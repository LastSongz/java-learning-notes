---
title: "AI大模型K8S集群架构面试题"
created: 2026-06-09
updated: 2026-06-09
tags:
  - 分类/ai
  - 分类/面试
  - 主题/Kubernetes
status: draft
category: interview
---

# 04 - AI 大模型 K8S 集群架构面试题

> 来源：`如何设计并优化运行AI大模型的K8S集群架构.md`。

## 一、GPU 资源选型

### 面试题

面对一个需要运行千亿参数大模型的 K8S 集群，如何选择 GPU？训练和推理的选型有什么区别？

### 回答要点

训练场景优先考虑：

- 大显存：能容纳模型权重、梯度、优化器状态。
- 高带宽：多卡通信是分布式训练瓶颈。
- 高速互联：NVLink / NVSwitch 对大模型训练很关键。

推理场景优先考虑：

- 显存容量：要放下模型权重和 KV Cache。
- 显存带宽：LLM 推理很多时候是 memory bound。
- 吞吐和成本：可以通过 MIG、MPS、量化等方式提高资源利用率。

### 面试话术

```
如果是训练，我会优先选择 A100 80G 或 H100 这类大显存、高带宽、NVLink 互联能力强的 GPU，因为训练阶段通信和模型状态开销很大。如果是推理，我会更关注显存容量、显存带宽和单位成本，结合量化、MIG 或 MPS 做资源复用。还要看 PCIe/NUMA 拓扑，避免把同一个分布式任务调度到跨 NUMA、通信很差的卡上。
```

## 二、K8S 集群架构设计

### 面试题

如何设计一个支持大规模 AI 训练的 K8S 集群？

### 回答要点

Master 节点：

- 3 或 5 节点高可用。
- Etcd 使用高性能 SSD/NVMe。
- 不运行普通业务 Pod。
- 大集群需要关注 API Server 的 QPS/Burst。

GPU 节点：

- 按训练、推理、CPU 预处理等角色分池。
- 使用 Label / Taint / Toleration 隔离负载。
- 安装 NVIDIA Driver、NVIDIA Container Toolkit、Device Plugin。
- 使用 Node Feature Discovery 暴露 GPU 型号、拓扑等信息。

网络：

- GPU 训练节点需要独立高速网络平面。
- 分布式训练的 NCCL 通信会产生大量东西向流量。
- 高端场景考虑 RoCE / InfiniBand / SR-IOV。

### 面试话术

```
我会把控制平面、GPU 训练节点、GPU 推理节点、CPU 预处理节点和存储节点分层设计。Master 节点做高可用，Etcd 用高性能本地盘；GPU 节点用 taint 隔离普通负载，并通过 Device Plugin 上报 nvidia.com/gpu 资源。网络上要单独规划高速东西向网络，避免分布式训练和普通业务流量互相影响。
```

## 三、调度与资源优化

### 面试题

一个 PyTorch 分布式训练任务需要 8 张 GPU，如何确保 8 个 Pod 同时调度成功并且通信效率高？

### 回答要点

- 原生调度器不支持 Gang Scheduling，可能出现部分 Pod 占着资源、任务却启动不了。
- 使用 Volcano 的 Gang Scheduling，保证“要么一起调度，要么都不调度”。
- 使用拓扑感知调度，优先调度到同一台 8 卡机器或同一高速网络域。
- 配置 NCCL 相关环境变量，例如高速网卡接口。

### 面试话术

```
我会用 Volcano 这类支持 Gang Scheduling 的调度器，避免 8 个 Pod 只启动了 7 个导致资源死锁。同时结合 Node Feature Discovery 和 GPU 拓扑信息，优先把 Pod 调度到同一台 8 卡 NVLink 机器上；如果必须跨机，就确保在同一高速网络域内，并配置 NCCL_SOCKET_IFNAME 等参数让通信走高速网卡。
```

## 四、存储与 IO 优化

### 面试题

训练时数据加载慢，GPU 利用率低，怎么优化？

### 回答要点

先判断瓶颈：

- CPU 预处理慢。
- 远端存储读取慢。
- 网络带宽不足。
- DataLoader 参数不合理。

优化方案：

- 用 Fluid + JuiceFS / Alluxio，把热点数据缓存到 GPU 节点本地 NVMe。
- 使用 RDMA、RoCE、InfiniBand 或 SR-IOV 降低网络开销。
- 对对象存储，不直接用低性能挂载方式，优先用 JuiceFS 这类云原生文件系统。
- 训练前预热数据，提高 Data Locality。

### 面试话术

```
GPU 利用率低不一定是 GPU 问题，很多时候是 IO 或 DataLoader 卡住了。我会先看 GPU 利用率、显存带宽、CPU、网络和存储指标。优化上可以把热点数据缓存到本地 NVMe，使用 JuiceFS/Alluxio 这类缓存层；网络上用 RDMA 或 SR-IOV；同时通过数据预热和亲和性调度，让任务尽量调度到已有缓存的节点。
```

## 五、监控与故障诊断

### 面试题

K8S 节点上的 NVIDIA GPU 变 Offline，或者 Pod 报 `NVIDIA driver/library version mismatch`，怎么排查？

### 回答步骤

1. `kubectl describe node` 查看 GPU 资源是否正常上报。
2. 登录节点执行 `nvidia-smi`。
3. 查看 Device Plugin Pod 日志。
4. 查内核日志：`dmesg | grep -i nvidia`。
5. 关注 NVIDIA XID 错误码。
6. 如果是驱动和内核不匹配，检查内核升级、DKMS 和驱动版本。

恢复：

- 轻度问题：重启 kubelet / containerd / docker。
- 严重问题：`cordon` + `drain` 节点后重启。
- 硬件问题：下线维修。

预防：

- DCGM Exporter 采集 GPU 温度、功耗、显存、PCIe/NVLink 错误。
- Node Problem Detector 自动标记异常节点。
- Prometheus + Alertmanager 告警。

## 六、生产级推理架构压轴题

### 题目

描述一套生产就绪的、运行千亿参数大模型推理服务的 K8S 架构，要求考虑弹性伸缩、灰度发布、成本和稳定性。

### 回答结构

接入层：

- Ingress / API Gateway。
- Istio 做灰度、基于 Header 的路由、流量治理。

调度层：

- Volcano 做 GPU 任务调度。
- Binpack 提高 GPU 利用率。
- 拓扑感知保证 Tensor Parallel 尽量在同机高速互联 GPU 上。

应用层：

- vLLM / KServe 承载推理。
- HPA 不看 CPU，而看排队请求数、吞吐、延迟、KV Cache 使用率等自定义指标。

基础设施层：

- H100/A100 GPU 节点。
- Cilium / eBPF 降低网络开销。
- JuiceFS / 对象存储保存模型权重。
- 模型预热，降低 Pod 启动和首次推理延迟。

稳定性：

- PDB 防止维护时全部实例不可用。
- Readiness / Liveness Probe 检测服务。
- Prometheus + DCGM + vLLM metrics 监控。
- 告警关注 TTFT、TPOT、队列长度、GPU 利用率、显存使用率、KV Cache 使用率。

## 关键要点

1. 训练重视大显存、高带宽、多卡互联；推理重视显存、吞吐、成本。
2. AI K8S 集群需要 GPU 节点隔离、Device Plugin、NFD 和高速网络。
3. 多 Pod 分布式训练要用 Gang Scheduling。
4. GPU 利用率低要从 IO、网络、DataLoader、存储缓存一起看。
5. 生产推理扩缩容应基于 LLM 自定义指标，而不是 CPU。

---

**相关笔记**：[[05-K8S部署vLLM推理框架实践]] | [[12-微调技术LoRA与QLoRA]] | [[AI项目面试话术]]
