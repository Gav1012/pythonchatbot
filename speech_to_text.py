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
        
        print("Hot Mic is Active...")
        # grabs from user's microphone
        result = self.speech_recognizer.recognize_once_async().get()
        # parses the result from the mic with currently 3 options to return
        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            print("found recognized speech".format(result.text))
        elif result.reason == speechsdk.ResultReason.NoMatch:
            print("no speech was recognized")
        elif result.reason == speechsdk.ResultReason.Canceled:
            print("speech recognition was cancelled")
        return result.text
    

    def transcribe_from_mic_continuous(self):
        self.audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
        self.speech_recognizer = speechsdk.SpeechRecognizer(speech_config=self.speech_config, audio_config=self.audio_config)

        done = False

        def stop_cb(evt):
            self.speech_recognizer.stop_continuous_recognition()
            nonlocal done
            done = True

        self.speech_recognizer.recognizing.connect(lambda evt: print('RECOGNIZING: {}'.format(evt)))
        self.speech_recognizer.recognized.connect(lambda evt: print('RECOGNIZED: {}'.format(evt)))
        # self.speech_recognizer.session_started.connect(lambda evt: print('SESSION STARTED: {}'.format(evt)))
        # self.speech_recognizer.session_stopped.connect(lambda evt: print('SESSION STOPPED {}'.format(evt)))
        # self.speech_recognizer.canceled.connect(lambda evt: print('CANCELED {}'.format(evt)))
        self.speech_recognizer.session_stopped.connect(stop_cb)
        self.speech_recognizer.canceled.connect(stop_cb)

        result_future = self.speech_recognizer.start_continuous_recognition_async()
        result_future.get()
        print('Continuous Recognition is now running, say something.')

        while not done:
            print('type "stop" then enter when done')
            stop = input()
            if (stop.lower() == "stop"):
                print('Stopping async recognition.')
                self.speech_recognizer.stop_continuous_recognition_async()
                break


# example of speech being used in file
if __name__ == '__main__':
    speechtotext_azure = AzureSpeechToText()
    
    # testing that microphone is being picked up and displaying the recognized speech
    while True:
        result = speechtotext_azure.transcribe_from_mic()
        print("RESULT: ", result)