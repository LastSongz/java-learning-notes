import asyncio

from _shared import build_llm, print_title


async def main() -> None:
    print_title("Demo 05: ainvoke() 异步调用")

    llm = build_llm()

    task = asyncio.create_task(
        llm.ainvoke("用一句话解释为什么 Web 服务里常用异步调用大模型。")
    )

    for index in range(3):
        await asyncio.sleep(1)
        print(f"等待模型返回时，主程序仍可执行其他任务：{index + 1}")

    response = await task
    print("\n模型回答:")
    print(response.content)


if __name__ == "__main__":
    asyncio.run(main())
