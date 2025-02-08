import os
from google.cloud import speech

class GoogleSpeechToText:
    def __init__(self, credentials_path):
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path
        self.client = speech.SpeechClient()

    def transcribe_audio(self, audio_path):
        with open(audio_path, 'rb') as audio_file:
            content = audio_file.read()
        audio = speech.RecognitionAudio(content=content)
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=16000,
            language_code='en-US'
        )
        response = self.client.recognize(config=config, audio=audio)
        return response.results[0].alternatives[0].transcript if response.results else ""
