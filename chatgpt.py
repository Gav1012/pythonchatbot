import os
import openai
from dotenv import load_dotenv
# loads openai api key from .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if api_key is None:
    raise ValueError("API not found")
openai.api_key = api_key

# main code to fulfill requests
def chat_a_bot(user_input):
    try:
        completion = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=user_input,
            max_tokens=200,
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"An error has occured: {str(e)}"
# starts a history tracker for all the responses between the bot and the user
bot_convo_history = [
    {"role": "system", "content": "You are Cayde-6 from the game series Destiny 2, and you only talk like you are him. Keep it in-universe."}
]
# makes the script continously run unless the user types 'exit'
while True:
    # grabs user input
    user_input = input("Message Cayde-6 (type 'exit' to quit): ")
    # way for user to end convo
    if user_input.lower() == 'exit':
        print("Goodbye, Guardian!")
        break
    # adds user input to the convo history
    bot_convo_history.append({"role": "user", "content": user_input})
    # bot takes new info from user to process with the previous history
    bot_response = chat_a_bot(bot_convo_history)
    # adds the bot's response to the history to be used later
    bot_convo_history.append({"role": "assistant", "content": bot_response})
    # outputs the response from the bot, in this case it's going to be cayde-6
    print("Cayde-6: ", bot_response)
