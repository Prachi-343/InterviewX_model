import librosa
import pydub
from google.cloud import speech

def process_audio(audio_data):
    # Preprocess audio
    audio = librosa.load(audio_data)
    # Convert to text using Google Speech-to-Text API
    client = speech.SpeechClient()
    response = client.recognize(audio=audio)
    transcription = response.results[0].alternatives[0].transcript
    return transcription