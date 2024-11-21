import os
from dotenv import load_dotenv
import azure.cognitiveservices.speech as speechsdk

class AzureSpeechToText:
    # handles the setup speech and language for Azure
    speech_config = None
    # handles the microphone/input
    audio_config = None
    # handles the processing of the speech to text format
    speech_recognizer = None
    def __init__(self):
        # loads .env file vals
        # attempts to use API key
        load_dotenv()
        try:
            self.speech_config = speechsdk.SpeechConfig(subscription=os.getenv("AZURE_SPEECH_KEY"), region=os.getenv("AZURE_REGION_KEY"))
        except TypeError:
            print("Error: Azure Speech Key or Region Key not found")
    
    # function to grab voice from mic and put it into text
    def transcribe_from_mic(self):
        # sets the microphone to device's default mic
        # sets up the recognizer using the speech config and the audio config settings
        self.audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
        self.speech_recognizer = speechsdk.SpeechRecognizer(speech_config=self.speech_config, audio_config=self.audio_config)

        print("Hot Mic Mode...")
        # grabs from user's microphone
        result = self.speech_recognizer.recognize_once_async().get()
        print(result.text)
        # parses the result from the mic with currently 3 options to return
        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            return print("found recognized speech".format(result.text))
        elif result.reason == speechsdk.ResultReason.NoMatch:
            return print("no speech was recognized")
        elif result.reason == speechsdk.ResultReason.Canceled:
            return print("speech recognition was cancelled")
        return result.text

# example of speech being used in file
if __name__ == '__main__':
    speechtotext_azure = AzureSpeechToText()
    
    # testing that microphone is being picked up and displaying the recognized speech
    while True:
        speechtotext_azure.transcribe_from_mic()