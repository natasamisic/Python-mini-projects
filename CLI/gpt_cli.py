from openai import OpenAI
#client = OpenAI(api_key="")

def ask_chatgpt(question):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo", 
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question},
            ],
        )
        return response.choices[0].message
    except Exception as e:
        return f"Error: {str(e)}"

print("Welcome to ChatGPT CLI! Type 'exit' to quit.")
while True:
    question = input("\nAsk ChatGPT: ")

    if question.lower() == 'exit':
        print("Goodbye!")
        break

    answer = ask_chatgpt(question)
    print(f"\nChatGPT: {answer}\n")