import unittest
from backend.utils.audio_processing import process_audio

class TestAudioProcessing(unittest.TestCase):
    def test_process_audio(self):
        # Mock audio data
        audio_data = "path/to/audio/file"
        # Call the function
        transcription = process_audio(audio_data)
        # Assert the transcription is not None
        self.assertIsNotNone(transcription)
        # Assert the transcription is a string
        self.assertIsInstance(transcription, str)

if __name__ == '__main__':
    unittest.main()