---
title: "K8S部署vLLM推理框架实践"
created: 2026-06-09
updated: 2026-06-09
tags:
  - 分类/ai
  - 分类/面试
  - 主题/vLLM
  - 主题/Kubernetes
status: draft
category: interview
---

# 05 - K8S 部署 vLLM 推理框架实践

> 来源：`202603-如何基于k8s集群运行AI大模型推理框架？.pdf`。该资料偏实操，适合准备“你是否真的部署过大模型推理服务”“K8S 上跑 vLLM 要注意什么”这类问题。

## 一、整体流程

```text
服务器与系统准备
  -> NVIDIA GPU 驱动
  -> Docker / cri-dockerd / container runtime
  -> NVIDIA Container Toolkit
  -> Kubernetes 集群
  -> Calico 网络插件
  -> NVIDIA Device Plugin
  -> NFS / PV / PVC
  -> vLLM Deployment / Service
  -> OpenAI API 兼容测试
  -> Open WebUI
  -> Prometheus + DCGM + Grafana 监控
```

## 二、基础设施准备

### 1. 节点规划

常见规划：

- `master`：控制平面。
- `worker`：GPU 工作节点。
- 独立 NFS 节点：存放模型权重和持久化数据。

面试时不要死背 IP 和命令，而要说明为什么这样分：

- 控制面和负载面隔离。
- GPU 节点统一安装驱动和容器运行时。
- 模型文件用共享存储，方便多个推理 Pod 读取。

### 2. GPU 驱动与容器运行时

关键组件：

- NVIDIA Driver：宿主机能识别 GPU。
- NVIDIA Container Toolkit：容器能访问 GPU。
- NVIDIA Device Plugin：K8S 能感知 `nvidia.com/gpu` 资源。

验证路径：

```text
宿主机 nvidia-smi 正常
  -> docker run --gpus all nvidia/cuda nvidia-smi 正常
  -> kubectl describe node 能看到 nvidia.com/gpu
  -> GPU Pod 能被调度并使用 GPU
```

## 三、K8S 集群准备

### 1. 网络插件

资料中使用 Calico。面试里可以这样讲：

```
K8S 集群初始化后节点通常还是 NotReady，需要安装 CNI 插件。Calico 负责 Pod 网络和网络策略。对于大模型训练或高性能推理，普通 CNI 可能不是瓶颈，但如果涉及跨节点高频通信，就要进一步考虑高速网络、RDMA 或 SR-IOV。
```

### 2. NVIDIA Device Plugin

Device Plugin 的作用：

- 发现节点 GPU。
- 向 kubelet 上报 `nvidia.com/gpu`。
- 在 Pod 调度后把 GPU 设备挂进容器。

面试话术：

```
K8S 本身不知道 GPU 这种扩展设备，需要 NVIDIA Device Plugin 通过 ListAndWatch 机制上报资源。上报成功后，我们就可以在 Pod 里声明 nvidia.com/gpu: 1，让调度器把它调度到 GPU 节点。
```

## 四、模型存储与 PV/PVC

资料中使用 NFS 做共享存储，把模型文件挂载给 vLLM。

面试表达：

```
vLLM 需要读取模型权重。简单环境可以用 NFS + PV/PVC，把模型目录挂载到 Pod 的 /models。生产环境要注意 NFS 性能和单点问题，更推荐高吞吐共享存储或对象存储加缓存层，例如 JuiceFS、Lustre、Alluxio 等。
```

需要关注：

- 模型文件很大，Pod 启动时加载慢。
- 多 Pod 同时拉模型会打爆存储。
- 模型目录权限和路径要稳定。
- 生产环境需要模型版本管理。

## 五、部署 vLLM

### 1. 核心参数

资料中可见的关键参数包括：

- `--model /models`
- `--served-model-name deepseek`
- `--max-model-len 8192`
- `--trust-remote-code`
- `--load-format safetensors`

面试时可以解释：

- `--model`：模型权重路径。
- `--served-model-name`：对外暴露的模型名。
- `--max-model-len`：最大上下文长度，影响 KV Cache 显存占用。
- `--trust-remote-code`：允许执行模型仓库自定义代码，要注意安全。
- `safetensors`：更安全、更快的权重格式。

### 2. 健康检查

vLLM 服务通常暴露：

- `/health`
- `/v1/models`
- `/v1/chat/completions`
- `/metrics`

K8S 里可以配置 readiness/liveness probe：

```text
readinessProbe -> /health
livenessProbe  -> /health
```

## 六、OpenAI 兼容接口测试

vLLM 的一个好处是兼容 OpenAI API 风格接口。

验证顺序：

1. `GET /v1/models` 确认模型列表。
2. `POST /v1/chat/completions` 做普通聊天。
3. 流式输出测试，确认 SSE/stream 正常。
4. 压测吞吐、TTFT、TPOT、并发队列。

面试话术：

```
部署完成后我不会只看 Pod Running，而会从接口层验证。先查 /v1/models，确认服务暴露的模型名；再用 OpenAI SDK 调 /v1/chat/completions；最后测试 stream 输出和并发性能。这样才能确认它是真的可用，而不是容器只是启动了。
```

## 七、Open WebUI

Open WebUI 可以作为演示和人工测试入口：

- 连接 vLLM 的 OpenAI 兼容接口。
- 提供网页聊天界面。
- 可用于内部体验和验收。

注意：生产环境不能只依赖 WebUI，要有 API 网关、鉴权、限流和审计。

## 八、监控体系

### 1. Prometheus

用于采集：

- K8S 资源指标。
- vLLM `/metrics`。
- NVIDIA DCGM Exporter 指标。

### 2. DCGM Exporter

关注 GPU 指标：

- GPU 利用率。
- 显存使用率。
- 显存拷贝带宽。
- 温度和功耗。
- ECC / XID 错误。

### 3. vLLM 指标

重点看：

- 请求排队数。
- KV Cache 使用率。
- TTFT：首 token 延迟。
- TPOT：每 token 输出耗时。
- 请求端到端延迟。
- Prompt / Generation token 数量。

### 4. Grafana 看板

面试里可以说自己会拆成两类看板：

- GPU 看板：资源利用率和硬件健康。
- vLLM 看板：请求、延迟、吞吐、KV Cache、错误率。

## 九、面试高频问题

### Q1：K8S 上部署 vLLM 的关键难点是什么？

```
难点不只是写 Deployment。第一是 GPU 能不能正确透传到容器，需要驱动、Container Toolkit 和 Device Plugin 都正常；第二是模型权重很大，存储和加载会影响启动速度；第三是显存容量和 max_model_len、batch、KV Cache 强相关；第四是生产环境要有健康检查、监控、告警和弹性伸缩。
```

### Q2：Pod Running 是否代表推理服务可用？

```
不代表。Pod Running 只能说明容器进程在跑。推理服务还要看模型是否加载完成、/health 是否正常、/v1/models 是否返回模型、chat completions 是否能响应、stream 是否正常，以及并发下延迟和显存是否稳定。
```

### Q3：如何做 vLLM 的扩缩容？

```
不能只看 CPU。更合理的是结合 vLLM 自定义指标，比如请求队列长度、TTFT、TPOT、KV Cache 使用率和 GPU 利用率。在线服务要避免频繁扩缩容，因为模型加载很慢，所以还要做预热、最小副本数和灰度发布。
```

### Q4：max_model_len 为什么会影响显存？

```
LLM 推理要保存 KV Cache，上下文越长，KV Cache 占用越大。max_model_len 设置越大，理论可支持的上下文越长，但显存压力也越高，吞吐可能下降。所以生产里要根据真实业务上下文长度设置，而不是盲目开很大。
```

## 关键要点

1. vLLM on K8S 的链路是 GPU 驱动、容器运行时、Device Plugin、存储、Deployment、Service、监控。
2. `nvidia.com/gpu` 能正常上报，是 K8S 使用 GPU 的关键。
3. 模型权重和 KV Cache 是推理部署的两个核心资源压力点。
4. vLLM 兼容 OpenAI API，可以用 SDK 或 curl 做端到端验证。
5. 生产扩缩容要看 LLM 自定义指标，而不是只看 CPU。

---

**相关笔记**：[[04-AI大模型K8S集群架构面试题]] | [[08-API开发]] | [[12-微调技术LoRA与QLoRA]]
