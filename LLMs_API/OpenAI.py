from openai import OpenAI

# Initialize the client (use OpenAI's API key)
# Replace with your OpenAI API key
client = OpenAI(api_key="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

# Initialize conversation history
conversation_history = [
    {"role": "system", "content": "You are a helpful assistant"}  # o1 does not support messages with the role "system"
]


def chat_with_assistant(user_input):
    # Add user input to the conversation history
    conversation_history.append({"role": "user", "content": user_input})

    # Call the API to generate a response (enable streaming)
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # Replace with OpenAI's model name
        # model="o1-preview",
        messages=conversation_history,
        stream=True  # Enable streaming
    )

    # Gradually display the assistant's response
    assistant_reply = ""
    # Print assistant prefix without a newline
    print("Assistant: ", end="", flush=True)
    for chunk in response:
        if chunk.choices[0].delta.content:  # Check if there is content
            content = chunk.choices[0].delta.content
            print(content, end="", flush=True)  # Print content incrementally
            assistant_reply += content  # Add content to the complete response

    # Add the assistant's response to the conversation history
    conversation_history.append(
        {"role": "assistant", "content": assistant_reply})

    return assistant_reply


# Example conversation
while True:
    user_input = input("You: ")  # User input
    if user_input.lower() in ["exit", "quit"]:
        print("Assistant: Goodbye!")
        break

    # Call the assistant and get a response
    chat_with_assistant(user_input)
    print("\n")  # Add a blank line after each conversation
