import os
import azure.cognitiveservices.speech as speechsdk

# subscription_key = API KEY
# service_region = REGION

# azure_speechconfig = None
# azure_audioconfig = None
# azure_speechrecognizer = None

azure_speechconfig = speech.sdk.SpeechConfig(subscription=subscription_key, region=region)

synthesizer = speechsdk.SpeechSynthesizer(azure_audioconfig=azure_audioconfig)

result = synthesizer.speak_text_async(text).get()
