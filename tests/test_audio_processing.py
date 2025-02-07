import unittest
from backend.utils.audio_processing import process_audio

class TestAudioProcessing(unittest.TestCase):
    def test_process_audio(self):
        audio_data = "path/to/audio/file"
        result = process_audio(audio_data)
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()