# imports from other supplemental files (more will be added)
from chatgpt import ChatGPTDirector
from speech_to_text import AzureSpeechToText

#sets up chatgpt class from chatgpt file
chatgpt_director = ChatGPTDirector()
azure_speech_to_text = AzureSpeechToText()
# use this to setup how the bot will behave including background and how it should respond
# this message will be added to kickstart the bot convo
INITIAL_MESSAGE = {"role": "system", "content": "You are Spider-Man and you will respond just like him"}

chatgpt_director.convo_history.append(INITIAL_MESSAGE)

# real meat and bones, where the bot will continue to work and respond
# want to add keyboard input to activate for when voice recognition is added
# might add a way to differentiate between using keyboard vs using microphone (might be affected by input/key)
while True:
    #user_input = input("type out a message to speak to a character (type 'exit to quit): ")
    user_input = azure_speech_to_text.transcribe_from_mic()
    chatgpt_director.exchange(user_input)