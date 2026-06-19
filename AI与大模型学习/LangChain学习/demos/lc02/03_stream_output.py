from _shared import build_llm, print_title


def main() -> None:
    print_title("Demo 03: stream() 流式输出")

    llm = build_llm()

    print("模型正在流式输出:\n")
    for chunk in llm.stream("用 120 字以内解释 Agent 和普通 LLM 调用的区别。"):
        print(chunk.content, end="", flush=True)
    print()


if __name__ == "__main__":
    main()
