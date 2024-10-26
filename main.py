from chatgpt import ChatGPTDirector

chatgpt_director = ChatGPTDirector()

INITIAL_MESSAGE = {"role": "system", "content": "You are Spider-Man and you will respond just like him"}

chatgpt_director.convo_history.append(INITIAL_MESSAGE)

while True:
    user_input = input("type out a message to speak to a character (type 'exit to quit): ")
    chatgpt_director.exchange(user_input)