from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

from _shared import build_llm, print_title


def main() -> None:
    print_title("Demo 02: Messages 对话调用")

    llm = build_llm()
    messages = [
        SystemMessage("你是一个技术面试教练，回答要简洁、有条理。"),
        HumanMessage("请用一句话解释什么是 RAG。"),
        AIMessage("RAG 是让大模型先检索外部资料，再基于资料生成答案的模式。"),
        HumanMessage("那它和普通 LLM 问答最大的区别是什么？"),
    ]

    response = llm.invoke(messages)

    print("模型回答:")
    print(response.content)


if __name__ == "__main__":
    main()
