import os
import azure.cognitiveservices.speech as speechsdk

def speech_to_text():
    # Replace with your own subscription key and service region (e.g., "eastus").
    subscription_key = "54644fee7ca94e449e1b8a7bf0ba0307"
    region = "eastus"
    
    # Creates an instance of a speech configuration with specified subscription key and region.
    speech_config = speechsdk.SpeechConfig(subscription=subscription_key, region=region)
    
    # Creates a speech recognizer using the default microphone as audio input.
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
    
    print("Say something...")
    
    # Starts speech recognition, and returns after a single utterance is recognized.
    result = speech_recognizer.recognize_once()
    
    # Checks result.
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(result.text))
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(result.no_match_details))
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))

if __name__ == "_main_": 
    speech_to_text()