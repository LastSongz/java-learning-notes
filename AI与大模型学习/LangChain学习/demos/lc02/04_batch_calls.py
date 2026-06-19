from _shared import build_llm, print_title


def main() -> None:
    print_title("Demo 04: batch() 批量调用")

    llm = build_llm()
    questions = [
        "用一句话解释 invoke。",
        "用一句话解释 stream。",
        "用一句话解释 batch。",
    ]

    print("batch() 会按输入顺序返回:\n")
    responses = llm.batch(questions, config={"max_concurrency": 3})
    for index, response in enumerate(responses, start=1):
        print(f"{index}. {response.content}")

    print("\nbatch_as_completed() 会按完成顺序返回:\n")
    for index, response in llm.batch_as_completed(
        questions, config={"max_concurrency": 3}
    ):
        print(f"原始问题下标 {index}: {response.content}")


if __name__ == "__main__":
    main()
