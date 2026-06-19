from _shared import build_llm, print_title


def main() -> None:
    print_title("Demo 01: invoke() 基础调用")

    llm = build_llm()
    response = llm.invoke("用三句话解释 LangChain 是什么。")

    print("返回对象类型:", type(response).__name__)
    print("模型回答:")
    print(response.content)


if __name__ == "__main__":
    main()
