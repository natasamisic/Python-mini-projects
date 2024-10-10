import os

from groq import Groq

# client = Groq(
#     api_key="",
# )

def ask_groq(question):
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "user", "content": question},
            ],
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

print("Welcome to Groq CLI! Type 'exit' to quit.")
while True:
    question = input("\nAsk Groq: ")

    if question.lower() == 'exit':
        print("Goodbye!")
        break

    answer = ask_groq(question)
    print(f"\nGroq: {answer}\n")