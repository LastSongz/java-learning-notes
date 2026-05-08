"""
AI Agent 实战：天气查询助手
用 GLM + Function Calling + Open-Meteo 免费天气 API

使用前：
1. 把下面的 API_KEY 改成你的 GLM API Key
2. 运行：python weather_agent.py
"""

# ==================== 导入库 ====================

# json 库：用来把 Python 字典和 JSON 字符串互相转换
# API 的请求和响应都是 JSON 格式，所以需要这个库
import json

# requests 库：用来发 HTTP 请求
# 我们用这个库去调用 Open-Meteo 的天气 API（免费的，不需要 Key）
import requests

# OpenAI 库：用来调用大模型的 API
# 虽然我们用的是 GLM（智谱），但 GLM 兼容 OpenAI 的接口格式
# 所以可以直接用 OpenAI 的库，只需要改一下 base_url
from openai import OpenAI


# ==================== 配置（填你的 Key）====================

# 你的 GLM API Key，去 open.bigmodel.cn 注册获取
API_KEY = "在这里填你的GLM_API_KEY"

# 创建大模型客户端
# api_key：你的密钥，证明你有权调用这个 API
# base_url：GLM 的服务器地址（不是 OpenAI 的服务器）
#   相当于告诉 OpenAI 库："别去 OpenAI 的服务器，去智谱的服务器"
client = OpenAI(
    api_key=API_KEY,
    base_url="https://open.bigmodel.cn/api/paas/v4"
)


# ==================== 工具函数（Agent 的"手和脚"）====================

# 常用城市 → 经纬度的映射字典
# Open-Meteo API 要求传经纬度，不支持直接传城市名
# 所以我们提前准备好常用城市的经纬度
# 格式："城市名": (纬度, 经度)
CITY_COORDS = {
    "北京": (39.9042, 116.4074),
    "上海": (31.2304, 121.4737),
    "广州": (23.1291, 113.2644),
    "深圳": (22.5431, 114.0579),
    "杭州": (30.2741, 120.1551),
    "成都": (30.5728, 104.0668),
    "武汉": (30.5928, 114.3055),
    "南京": (32.0603, 118.7969),
    "西安": (34.3416, 108.9398),
    "重庆": (29.4316, 106.9123),
    "天津": (39.3434, 117.3616),
    "苏州": (31.2990, 120.5853),
    "长沙": (28.2282, 112.9388),
    "郑州": (34.7466, 113.6253),
    "厦门": (24.4798, 118.0894),
}


# ---------- 工具1：查询天气 ----------

def get_weather(city: str) -> str:
    """
    调用 Open-Meteo 免费天气 API 查询指定城市的天气
    参数 city：城市名（如 "北京"）
    返回：JSON 格式的天气数据字符串
    """

    # 第一步：把城市名转成经纬度
    if city not in CITY_COORDS:
        # 如果城市不在预置字典里，就用 Geocoding API（地名→经纬度）
        # 这是 Open-Meteo 提供的另一个免费 API
        try:
            geo_url = "https://geocoding-api.open-meteo.com/v1/search"
            # 发 GET 请求，传参：
            #   name=城市名，count=只要第一个结果，language=zh 中文
            geo_resp = requests.get(geo_url, params={
                "name": city,
                "count": 1,
                "language": "zh"
            }, timeout=10)  # timeout=10 表示最多等10秒
            geo_data = geo_resp.json()  # 把响应转成 Python 字典

            if geo_data.get("results"):
                # 找到了 → 取出经纬度
                lat = geo_data["results"][0]["latitude"]   # 纬度
                lon = geo_data["results"][0]["longitude"]  # 经度
                city_name = geo_data["results"][0].get("name", city)
            else:
                # 没找到 → 返回错误信息
                return json.dumps({"error": f"找不到城市: {city}"}, ensure_ascii=False)
        except Exception as e:
            # 网络错误等异常 → 返回错误信息
            return json.dumps({"error": f"查找城市失败: {str(e)}"}, ensure_ascii=False)
    else:
        # 城市在预置字典里 → 直接取经纬度
        lat, lon = CITY_COORDS[city]
        city_name = city

    # 第二步：用经纬度调用天气 API
    try:
        url = "https://api.open-meteo.com/v1/forecast"  # 天气 API 地址
        params = {
            "latitude": lat,      # 纬度
            "longitude": lon,    # 经度
            "current": "temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m",
            "daily": "temperature_2m_max,temperature_2m_min,weather_code",
            "timezone": "Asia/Shanghai",
            "forecast_days": 3
        }
        resp = requests.get(url, params=params, timeout=10)
        data = resp.json()

        # 天气代码 → 中文描述的映射字典
        weather_map = {
            0: "晴天", 1: "大部晴朗", 2: "多云", 3: "阴天",
            45: "雾", 48: "冻雾",
            51: "小雨", 53: "中雨", 55: "大雨",
            61: "小雨", 63: "中雨", 65: "大雨",
            71: "小雪", 73: "中雪", 75: "大雪",
            80: "阵雨", 81: "中阵雨", 82: "大阵雨",
            95: "雷暴", 96: "雷暴冰雹",
        }

        current = data["current"]
        daily = data["daily"]

        result = {
            "city": city_name,
            "current": {
                "temperature": f"{current['temperature_2m']}°C",
                "humidity": f"{current['relative_humidity_2m']}%",
                "weather": weather_map.get(current['weather_code'], "未知"),
                "wind_speed": f"{current['wind_speed_10m']} km/h"
            },
            "forecast": []
        }

        for i in range(len(daily["time"])):
            result["forecast"].append({
                "date": daily["time"][i],
                "weather": weather_map.get(daily["weather_code"][i], "未知"),
                "temp_max": f"{daily['temperature_2m_max'][i]}°C",
                "temp_min": f"{daily['temperature_2m_min'][i]}°C"
            })

        return json.dumps(result, ensure_ascii=False, indent=2)

    except Exception as e:
        return json.dumps({"error": f"天气查询失败: {str(e)}"}, ensure_ascii=False)


# ---------- 工具2：计算器 ----------

def calculate(expression: str) -> str:
    """
    安全计算数学表达式
    参数 expression：数学表达式字符串（如 "25 - 22"）
    返回：计算结果字符串
    """
    try:
        allowed = set("0123456789+-*/.() ")
        if not all(c in allowed for c in expression):
            return "表达式包含不允许的字符"
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"计算错误: {str(e)}"


# ==================== Agent 核心逻辑 ====================

# ---------- 告诉模型"你有哪些工具可用" ----------
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "查询指定城市的实时天气和未来3天预报，支持国内任意城市",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "城市名称，如：北京、上海、成都"
                    }
                },
                "required": ["city"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculate",
            "description": "计算数学表达式，如：25 - 22、100 * 0.8",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "数学表达式，如：25 - 22"
                    }
                },
                "required": ["expression"]
            }
        }
    }
]

# 工具名 → 实际函数的映射
TOOL_FUNCTIONS = {
    "get_weather": get_weather,
    "calculate": calculate,
}


# ---------- Agent 核心循环（支持流式输出）----------

def chat_stream(user_input: str, messages: list):
    """
    Agent 核心循环（流式版本）：思考 → 调工具 → 再思考 → 流式输出回答

    参数：
        user_input: 用户输入的文字
        messages: 对话历史列表（会被修改，保持对话上下文）
    返回：生成器，每次 yield 一个字符（流式输出）
    """

    # 把用户消息加入对话历史
    messages.append({"role": "user", "content": user_input})

    # Agent 循环：最多跑5轮
    for _ in range(5):

        # 第一阶段：调用大模型 API（非流式）
        # 这里不用 stream=True，因为我们需要等所有 tool_calls 都返回了
        # 才能知道模型要不要调工具、调哪些工具
        response = client.chat.completions.create(
            model="glm-4-flash",
            messages=messages,
            tools=tools
        )

        message = response.choices[0].message

        # 判断：模型是想直接回答，还是想调工具？
        if not message.tool_calls:
            # 模型直接回答 → 启用流式输出，边生成边 yield
            messages.append({"role": "assistant", "content": ""})

            # 再次请求，但这次开启流式
            stream_response = client.chat.completions.create(
                model="glm-4-flash",
                messages=messages,
                tools=tools,
                stream=True  # ← 开启流式
            )

            # 遍历流式返回的每个 chunk（每个 chunk 包含一小段文字）
            for chunk in stream_response:
                # chunk.choices[0].delta.content 是这段 chunk 的文字内容
                # 有些 chunk 可能是空的（只有 role 等信息），要跳过
                content = chunk.choices[0].delta.content
                if content:
                    # 累积到对话历史里（保持上下文完整）
                    messages[-1]["content"] += content
                    # yield出去（让调用方能实时看到）
                    yield content

            # 流式输出结束，跳出生成器
            return

        # 模型想调工具 → 执行工具（工具调用是非流式的，很快）
        messages.append(message)

        for tool_call in message.tool_calls:
            fn_name = tool_call.function.name
            fn_args = json.loads(tool_call.function.arguments)

            # 打印日志
            print(f"  🔧 调用工具: {fn_name}({fn_args})", flush=True)

            # 执行工具
            result = TOOL_FUNCTIONS[fn_name](**fn_args)
            print(f"  📦 工具结果: {result[:100]}...", flush=True)

            # 把工具结果喂回模型
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": result
            })

        # 工具执行完 → 回到循环开头，模型看到结果后继续思考


# ==================== 主程序（入口）====================

def main():
    """主函数：程序从这里开始执行"""

    # 打印欢迎信息
    print("=" * 50)
    print("🌤️  天气查询 Agent（输入 q 退出）")
    print("=" * 50)
    print("你可以问：")
    print("  - 北京今天天气怎么样？")
    print("  - 上海和杭州哪边更热？差几度？")
    print("  - 这周末深圳适合出去玩吗？")
    print()

    # 初始化对话历史
    messages = [
        {"role": "system", "content": """你是一个天气助手，可以查询天气和做简单计算。
回答要简洁友好，使用中文。
如果用户问多个城市的天气，分别查询后做对比。
温度对比时可以用 calculate 工具计算温差。"""}
    ]

    # 主循环：不断等待用户输入
    while True:
        user_input = input("\n🙋 你: ").strip()
        if user_input.lower() in ("q", "quit", "退出"):
            print("👋 再见！")
            break
        if not user_input:
            continue

        print("\n🤖 天气助手: ", end="", flush=True)

        # 调用 Agent（流式版本），边生成边打印
        # chat_stream 是一个生成器，每次 yield 一小段文字
        reply_chars = []
        for char in chat_stream(user_input, messages):
            print(char, end="", flush=True)  # 实时打印字符（不换行）
            reply_chars.append(char)

        print()  # 最后换行


# Python 的入口写法
if __name__ == "__main__":
    main()