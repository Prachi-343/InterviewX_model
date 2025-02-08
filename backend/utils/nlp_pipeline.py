import librosa
from google.cloud import speech
from difflib import SequenceMatcher

class NLPPipeline:
    def __init__(self):
        self.speech_client = speech.SpeechClient()

    def preprocess_audio(self, audio_path):
        y, sr = librosa.load(audio_path, sr=16000)
        return y, sr

    def transcribe_audio(self, audio_path):
        y, sr = self.preprocess_audio(audio_path)
        audio = speech.RecognitionAudio(content=y.tobytes())
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=sr,
            language_code="en-US",
        )

        response = self.speech_client.recognize(config=config, audio=audio)
        transcription = response.results[0].alternatives[0].transcript
        return transcription

    def compare_answers(self, user_answer, expected_answer):
        similarity = SequenceMatcher(None, user_answer, expected_answer).ratio()
        return similarity

    def process_audio(self, audio_path, expected_answer):
        transcription = self.transcribe_audio(audio_path)
        similarity = self.compare_answers(transcription, expected_answer)
        return transcription, similarity