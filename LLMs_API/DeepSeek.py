from openai import OpenAI

# 初始化客户端
client = OpenAI(api_key="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                base_url="https://api.deepseek.com")

# 初始化对话历史
conversation_history = [
    {"role": "system", "content": "You are a helpful assistant"}
]


def chat_with_assistant(user_input):
    # 将用户输入添加到对话历史中
    conversation_history.append({"role": "user", "content": user_input})

    # 调用API生成回复（启用流式传输）
    response = client.chat.completions.create(
        model="deepseek-chat", 
        # model="deepseek-reasoner",
        messages=conversation_history,
        stream=True  # 启用流式传输
    )

    # 逐步显示助手的回复
    assistant_reply = ""
    print("Assistant: ", end="", flush=True)  # 打印助手前缀，不换行
    for chunk in response:
        if chunk.choices[0].delta.content:  # 检查是否有内容
            content = chunk.choices[0].delta.content
            print(content, end="", flush=True)  # 逐字打印
            assistant_reply += content  # 将内容添加到完整回复中

    # 将助手的回复添加到对话历史中
    conversation_history.append(
        {"role": "assistant", "content": assistant_reply})

    return assistant_reply


# 示例对话
while True:
    user_input = input("You: ")  # 用户输入
    if user_input.lower() in ["exit", "quit"]:
        print("Assistant: Goodbye!")
        break

    # 调用助手并获取回复
    chat_with_assistant(user_input)
    print("\n")  # 在每组对话后添加空行
