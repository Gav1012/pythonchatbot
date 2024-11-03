import os
from dotenv import load_dotenv
import azure.cognitiveservices.speech as speechsdk

class AzureSpeechToText:
    def __init__(self):
        load_dotenv()
        try:
            self.azure_speechconfig = speechsdk.SpeechConfig(subscription=os.getenv("AZURE_SPEECH_KEY"), region=os.getenv("AZURE_REGIONKEY"))
        except TypeError:
            print("Error: Azure Speech Key or Region Key not found")
    
    def transcribe_from_mic(self):
        audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=self.speech_config, audio_config=audio_config)

        print("Hot Mic Mode...")

        result = speech_recognizer.recognize_once()

        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            return result.text
        elif result.reason == speechsdk.ResultReason.NoMatch:
            return "No Match"
        elif result.reason == speechsdk.ResultReason.Canceled:
            return "Speech Cancelled"

if __name__ == '__main__':
    speechtotext_azure = AzureSpeechToText()