import os
import openai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("CHATGPT_API_KEY")

# print("API KEY: ", api_key)

ai_response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are Cayde-6 from the game series Destiny 2"},
        {"role": "user", "content": "What is your favorite food?"}
    ]
)

print(ai_response["choices"][0]["message"]["content"])
