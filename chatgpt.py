import os
import openai
from dotenv import load_dotenv
# loads openai api key from .env file
load_dotenv()
api_key = os.getenv("CHATGPT_API_KEY")

user_input = input("Enter your prompt to ask the Bot: ")

# main code to fulfill requests
completion = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are Cayde-6 from the game series Destiny 2, and you only talk like you are him. Keep it in-universe"},
        {"role": "user", "content": user_input}
    ]
)

print(completion.choices[0].message.content)
