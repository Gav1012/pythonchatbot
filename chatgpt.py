import os
from openai import OpenAI
from dotenv import load_dotenv

# class that holds the main processing of prompts with OpenAI AI
class ChatGPTDirector:
    def __init__(self):
        self.convo_history = []
        # loads openai api key from .env file
        load_dotenv()
        try:
            self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        except TypeError:
            exit("No OPEN_API_KEY found")
    # processes the user input, being able to build off the the previous conversations
    def exchange(self, prompt=""):
        if not prompt:
            print("nothing was recorded")
            return
        # adds user input to the history for AI to reference in the future
        self.convo_history.append({"role": "user", "content": prompt})
        # does the actual computations
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=self.convo_history,
            max_tokens=200,
        )
        # adds AI reponse to the history
        self.convo_history.append({"role": completion.choices[0].message.role, "content": completion.choices[0].message.content})
        response = completion.choices[0].message.content
        print(response)
        return response


if __name__ == '__main__':
    chatgpt_dir = ChatGPTDirector()
    # chatgpt_dir.exchange("Hello, how are you?")
    # example of giving the AI background of what it's going to be/behave/etc and appends directly to history
    # this part can be changed out to any character that you want, this is just for an example
    cayde_history_test = {"role": "system", "content": "You are Cayde-6 from the game series Destiny by Bungie, and you only talk like you are him. Keep it in-universe."}
    chatgpt_dir.convo_history.append(cayde_history_test)
    # continously allows user to message the ai
    while True:
        user_input = input("type out message to Cayde-6 (type 'exit' to quit): ")
        chatgpt_dir.exchange(user_input)

