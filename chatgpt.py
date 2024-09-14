import os
import openai
from dotenv import load_dotenv
# loads openai api key from .env file
load_dotenv()
api_key = os.getenv("CHATGPT_API_KEY")

if api_key is None:
    raise ValueError("API not found")

# main code to fulfill requests
def chat_a_bot(input):
    try:
        completion = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are Cayde-6 from the game series Destiny 2, and you only talk like you are him. Keep it in-universe"},
                {"role": "user", "content": input}
            ],
            max_tokens=500,
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"An error has occured: {str(e)}"

user_input = input("Enter your prompt to ask the Bot: ")

output = chat_a_bot(user_input)
print(output)