from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
)


BASE_DIR = Path(__file__).resolve().parent
OUTPUT = BASE_DIR / "6年-Java-本科.pdf"


def register_fonts() -> None:
    pdfmetrics.registerFont(TTFont("CN-Regular", r"C:\Windows\Fonts\simsun.ttc"))
    pdfmetrics.registerFont(TTFont("CN-Bold", r"C:\Windows\Fonts\simhei.ttf"))
    pdfmetrics.registerFontFamily(
        "CN",
        normal="CN-Regular",
        bold="CN-Bold",
        italic="CN-Regular",
        boldItalic="CN-Bold",
    )


def make_styles() -> dict[str, ParagraphStyle]:
    base = {
        "wordWrap": "CJK",
    }
    return {
        "name": ParagraphStyle(
            "name",
            **base,
            fontName="CN-Bold",
            fontSize=20,
            leading=24,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#222222"),
            spaceAfter=3,
        ),
        "headline": ParagraphStyle(
            "headline",
            **base,
            fontName="CN-Regular",
            fontSize=9.6,
            leading=12,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#333333"),
            spaceAfter=6,
        ),
        "section": ParagraphStyle(
            "section",
            **base,
            fontName="CN-Bold",
            fontSize=11.2,
            leading=14,
            textColor=colors.HexColor("#111111"),
            borderWidth=0,
            borderColor=colors.HexColor("#333333"),
            borderPadding=0,
            spaceBefore=6,
            spaceAfter=4,
        ),
        "body": ParagraphStyle(
            "body",
            **base,
            fontName="CN-Regular",
            fontSize=8.6,
            leading=12.1,
            textColor=colors.HexColor("#222222"),
            firstLineIndent=0,
            spaceAfter=2.4,
        ),
        "compact": ParagraphStyle(
            "compact",
            **base,
            fontName="CN-Regular",
            fontSize=8.25,
            leading=11.4,
            textColor=colors.HexColor("#222222"),
            spaceAfter=1.8,
        ),
        "project": ParagraphStyle(
            "project",
            **base,
            fontName="CN-Bold",
            fontSize=10,
            leading=12.8,
            textColor=colors.HexColor("#111111"),
            spaceBefore=5,
            spaceAfter=3,
        ),
        "label": ParagraphStyle(
            "label",
            **base,
            fontName="CN-Bold",
            fontSize=8.7,
            leading=11.8,
            spaceBefore=2,
            spaceAfter=1.5,
        ),
    }


def p(text: str, style: ParagraphStyle) -> Paragraph:
    return Paragraph(text, style)


def bullet(text: str, style: ParagraphStyle) -> Paragraph:
    return Paragraph(f"• {text}", style)


def section(title: str, styles: dict[str, ParagraphStyle]) -> list:
    return [
        Spacer(1, 2),
        p(f"<b>{title}</b>", styles["section"]),
        Spacer(1, 1),
    ]


def add_page_number(canvas, doc) -> None:
    canvas.saveState()
    canvas.setFont("CN-Regular", 7.5)
    canvas.setFillColor(colors.HexColor("#666666"))
    canvas.drawCentredString(A4[0] / 2, 7.5 * mm, f"{doc.page}")
    canvas.restoreState()


def build_story(styles: dict[str, ParagraphStyle]) -> list:
    story: list = []

    story.append(p("宋凯旋", styles["name"]))
    story.append(
        p(
            "男｜29 岁｜<b>6 年以上 Java 后端开发经验</b>｜电话：19136090559｜邮箱：skyrim54@163.com",
            styles["headline"],
        )
    )
    story.append(
        p("求职意向：<b>高级 Java 开发工程师</b>｜期望城市：成都", styles["headline"])
    )

    story += section("个人优势", styles)
    for item in [
        "<b>6 年以上 Java 后端开发经验</b>，近 4 年参与华为海思芯片供应链核心系统建设，熟悉制造、权限治理、供应链协同等复杂业务场景。",
        "有 <b>DDD 重构落地经验</b>，参与制造域、用户中心等核心模块的领域建模、聚合边界划分、遗留逻辑迁移和分层架构治理。",
        "熟悉分布式一致性、缓存、消息和权限相关场景，实践过 <b>Transactional Outbox、CDC、消费幂等、多级缓存和多租户权限隔离</b>。",
        "有工程质量治理经验，参与 <b>代码评审、单元测试覆盖率要求、CI 质量门禁、上线 Checklist、回滚方案</b>和新人指导。",
        "参与供应链智能聊天助手建设，熟悉 <b>Tool 能力接入、权限动态裁剪、微组件确认和 Spring SseEmitter 流式响应</b>等 AI 应用后端场景。",
    ]:
        story.append(bullet(item, styles["compact"]))

    story += section("专业技能", styles)
    for item in [
        "<b>Java 与微服务</b>：熟悉 Java 后端开发，熟悉 Spring Boot、Spring Cloud Alibaba、MyBatis 等常用技术栈，了解 JDK 21 虚拟线程等新特性。",
        "<b>架构与建模</b>：有 DDD 战略设计、战术建模和领域边界划分实践，能够结合复杂业务拆分聚合、领域服务和应用服务职责。",
        "<b>分布式与中间件</b>：熟悉 Redis、RocketMQ、CDC、Transactional Outbox、消费幂等、重试和最终一致性处理。",
        "<b>数据库</b>：熟悉 PostgreSQL、Oracle、MySQL，具备表结构设计、复杂 SQL 梳理、索引优化和 Oracle 存储过程迁移经验。",
        "<b>工程实践</b>：熟悉代码评审、单元测试、CI 门禁、上线 Checklist、灰度发布和回滚方案等交付质量保障手段。",
        "<b>AI 辅助研发</b>：日常使用 Codex 辅助代码理解、问题排查、测试补充和文档整理，能结合项目规范控制输出质量。",
    ]:
        story.append(bullet(item, styles["compact"]))

    story += section("工作经历", styles)
    story.append(
        p(
            "<b>中软国际科技服务有限公司｜Java 开发工程师｜2021.11 - 至今</b>",
            styles["body"],
        )
    )
    for item in [
        "服务华为海思芯片供应链系统，参与制造域、用户中心、花聊智能助手等模块建设。",
        "负责需求分析、后端开发、方案设计、代码评审和上线支持。",
        "参与 DDD 重构、权限治理、智能助手能力接入和工程质量改进。",
    ]:
        story.append(bullet(item, styles["compact"]))
    story.append(
        p(
            "<b>中通服创立科技有限公司｜Java 开发工程师 / 企业服务器运维｜2019.12 - 2021.11</b>",
            styles["body"],
        )
    )
    for item in [
        "参与企业内部系统开发和服务器运维工作。",
        "负责业务功能开发、Linux 服务器维护、监控告警配置和日常问题处理。",
    ]:
        story.append(bullet(item, styles["compact"]))

    story += section("项目经历", styles)
    story.append(
        p(
            "海思芯片供应链交付系统 - DDD 架构重构｜需求分析与后端开发｜2024.05 - 至今",
            styles["project"],
        )
    )
    story.append(p("<b>项目背景：</b>", styles["label"]))
    story.append(
        p(
            "海思芯片供应链系统经过多年迭代，Java 代码与 Oracle 存储过程耦合较重，部分核心业务逻辑沉淀在复杂存储过程中，导致需求变更成本高、问题定位困难。项目采用 DDD 思路逐步重构，将核心业务逻辑迁移到新的微服务体系中。",
            styles["compact"],
        )
    )
    story.append(p("<b>主要职责：</b>", styles["label"]))
    for i, item in enumerate(
        [
            "<b>领域建模：</b>负责制造域 DDD 重构相关开发，参与需求分析、方案串讲、战略设计和战术设计文档编写。",
            "<b>聚合设计：</b>参与制造域建模，梳理 <b>buildPlan、工单、工单上传</b>等核心聚合，明确聚合边界和一致性要求。",
            "<b>遗留迁移：</b>参与 Oracle 存储过程逻辑拆解，将部分复杂存储过程迁移到 Java 服务中，降低后续维护成本。",
            "<b>核心开发：</b>作为制造域团队核心开发，负责核心聚合与应用服务的代码设计、评审和重构落地，推动团队在分层、命名、单元测试和 Clean Code 方面保持一致。",
            "<b>上线治理：</b>推动上线 Checklist 标准化，覆盖脚本、配置、API 订阅、MQ 发布订阅、权限点、验证方案和回滚方案。",
        ],
        1,
    ):
        story.append(p(f"{i}. {item}", styles["compact"]))
    story.append(p("<b>关键成果：</b>", styles["label"]))
    for i, item in enumerate(
        [
            "识别工单与工单上传聚合边界不清的问题，结合生命周期、状态流转和事务边界，将工单上传拆分为独立聚合，减少聚合职责混杂。",
            "采用<b>绞杀者模式</b>逐步迁移遗留逻辑，降低一次性重构风险。",
            "通过 <b>Transactional Outbox + CDC</b> 保证业务操作与事件发布的一致性，消费端基于业务唯一键实现幂等。",
            "将代码检查、单元测试覆盖率和需求单关联校验接入 <b>CI 门禁</b>，减少未关联需求、测试覆盖不足或代码规范不达标的提交进入主干。",
        ],
        1,
    ):
        story.append(p(f"{i}. {item}", styles["compact"]))

    story.append(PageBreak())

    story.append(
        p(
            "用户中心 - 供应链统一权限治理平台｜项目负责人｜2023.12 - 2025.01",
            styles["project"],
        )
    )
    story.append(p("<b>项目背景：</b>", styles["label"]))
    story.append(
        p(
            "用户中心面向供应链多角色、多租户、多数据维度的权限治理场景，包含菜单管理、角色管理、用户管理、领域管理、首页、公告和站内消息等功能。",
            styles["compact"],
        )
    )
    story.append(p("<b>主要职责：</b>", styles["label"]))
    for i, item in enumerate(
        [
            "<b>需求设计：</b>负责需求收集、功能设计和后端开发，参与用户中心 DDD 建模和聚合划分。",
            "<b>权限扩展：</b>基于企业通用权限框架进行扩展，补充<b>多租户隔离、角色权限切换和数据维度控制</b>能力。",
            "<b>链路改造：</b>参与权限校验链路改造，支持按领域、角色、菜单和数据维度进行权限控制。",
            "<b>团队协作：</b>负责项目进度跟踪、代码评审、新人指导和测试用例评审，保障版本按计划交付。",
        ],
        1,
    ):
        story.append(p(f"{i}. {item}", styles["compact"]))
    story.append(p("<b>关键成果：</b>", styles["label"]))
    for i, item in enumerate(
        [
            "针对页面频繁调用的用户权限查询接口，引入 <b>Caffeine + Redis 多级缓存</b>，本地缓存承接高频读取，Redis 缓存支撑跨实例共享，并结合权限变更设计缓存失效策略；优化后<b>单机 QPS 从 200 提升到 2000+</b>，平均响应耗时压降至 <b>10ms 级</b>。",
            "扩展多租户权限模型，支持用户切换租户后自动切换角色权限，满足供应链多参与方权限隔离需求。",
            "通过源码阅读和权限拦截逻辑改造，将权限控制从菜单级扩展到领域和数据维度，支持更细粒度的数据访问控制。",
        ],
        1,
    ):
        story.append(p(f"{i}. {item}", styles["compact"]))

    story.append(
        p(
            "花聊 - 供应链智能聊天助手｜Java 后端开发｜2025.01 - 至今",
            styles["project"],
        )
    )
    story.append(p("<b>项目背景：</b>", styles["label"]))
    story.append(
        p(
            "花聊是面向供应链业务用户的智能聊天助手，支持基于知识库回答系统操作问题，也支持在用户具备权限的前提下查询业务数据、发起业务操作。查询结果通过卡片式微组件展示在聊天框中；涉及创建 buildPlan 等写操作时，系统会先生成表单微组件，由用户确认后主动提交，并在提交链路中再次进行权限校验。",
            styles["compact"],
        )
    )
    story.append(p("<b>主要职责：</b>", styles["label"]))
    for i, item in enumerate(
        [
            "<b>会话管理：</b>参与花聊后端接口开发，支持前端创建会话、获取用户会话，并维护用户会话上下文。",
            "<b>流式响应：</b>基于 <b>Spring SseEmitter</b> 实现聊天消息流式响应，后端在模型生成过程中分段推送内容，前端实时渲染输出结果。",
            "<b>Tool 设计：</b>参与权限感知的 <b>Tool Registry</b> 机制设计，将操作指导、数据查询、业务操作抽象为三类 Tool，并按用户角色、租户和数据权限动态裁剪可用能力。",
            "<b>能力接入：</b>参与供应链业务能力接入，将数据查询、创建 buildPlan 等能力封装为可被聊天助手编排的业务工具。",
            "<b>微组件联动：</b>配合前端完成微组件展示方案，查询类结果返回卡片组件，操作类请求返回表单组件，由用户确认后再提交执行。",
        ],
        1,
    ):
        story.append(p(f"{i}. {item}", styles["compact"]))
    story.append(p("<b>关键成果：</b>", styles["label"]))
    for i, item in enumerate(
        [
            "落地权限感知的 Tool Registry 机制，按操作指导、数据查询、业务操作三类场景动态返回当前用户可用能力，避免模型访问或触发无权限业务能力。",
            "对读写操作做分层控制：查询类能力在权限校验后返回结构化卡片，创建类操作必须由用户确认并主动提交。",
            "通过“文本回答 + 卡片微组件 + 表单确认”的方式，将聊天助手从单纯问答扩展为海思芯片供应链业务入口。",
        ],
        1,
    ):
        story.append(p(f"{i}. {item}", styles["compact"]))

    story.append(
        p(
            "海思芯片供应链交付系统 - 核心业务迭代｜Java 后端开发｜2021.11 - 2023.11",
            styles["project"],
        )
    )
    story.append(p("<b>项目背景：</b>", styles["label"]))
    story.append(
        p(
            "系统覆盖需求计划、订单、生产制造、物流协同等海思芯片供应链核心链路，服务海思芯片供应与交付业务。项目长期迭代，存在需求链路长、业务规则复杂、历史 SQL 和存储过程较多等特点。",
            styles["compact"],
        )
    )
    story.append(p("<b>主要职责：</b>", styles["label"]))
    for i, item in enumerate(
        [
            "<b>模块开发：</b>负责核心业务模块后端开发，参与需求分析、接口设计、数据库设计和上线支持。",
            "<b>流程联调：</b>参与复杂业务流梳理，配合业务方、测试和上下游系统完成需求对齐与联调验证。",
            "<b>问题排查：</b>参与线上问题排查和历史 SQL 梳理，针对部分低效查询和存储过程进行优化。",
            "<b>部署支持：</b>维护 Linux 环境下的应用部署、日志排查和基础监控告警，保障版本上线后的问题响应。",
        ],
        1,
    ):
        story.append(p(f"{i}. {item}", styles["compact"]))
    story.append(p("<b>关键成果：</b>", styles["label"]))
    for i, item in enumerate(
        [
            "参与多项海思芯片供应链核心流程的接口开发和联调，熟悉计划、制造、物流等模块之间的数据流转关系。",
            "在长期迭代系统中持续处理需求变更、缺陷修复和上线支持，为后续 DDD 重构积累业务链路理解。",
        ],
        1,
    ):
        story.append(p(f"{i}. {item}", styles["compact"]))

    story += section("教育经历", styles)
    story.append(p("<b>绵阳师范学院｜物流管理｜本科｜2015.09 - 2019.06</b>", styles["body"]))

    story += section("资格证书", styles)
    story.append(p("大学英语四级｜计算机二级｜<b>Harness Developer</b>", styles["body"]))

    return story


def main() -> None:
    register_fonts()
    styles = make_styles()

    doc = BaseDocTemplate(
        str(OUTPUT),
        pagesize=A4,
        rightMargin=18 * mm,
        leftMargin=18 * mm,
        topMargin=12 * mm,
        bottomMargin=12 * mm,
    )
    frame = Frame(
        doc.leftMargin,
        doc.bottomMargin,
        doc.width,
        doc.height,
        leftPadding=0,
        rightPadding=0,
        topPadding=0,
        bottomPadding=0,
    )
    template = PageTemplate(id="resume", frames=[frame], onPage=add_page_number)
    doc.addPageTemplates([template])
    doc.build(build_story(styles))
    print(OUTPUT)


if __name__ == "__main__":
    main()
