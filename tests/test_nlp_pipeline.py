import unittest
from backend.utils.nlp_pipeline import NLPPipeline

class TestNLPPipeline(unittest.TestCase):
    def setUp(self):
        self.nlp_pipeline = NLPPipeline()

    def test_transcribe_audio(self):
        # Mock audio data
        audio_data = "path/to/audio/file"
        # Call the function
        transcription = self.nlp_pipeline.transcribe_audio(audio_data)
        # Assert the transcription is not None
        self.assertIsNotNone(transcription)
        # Assert the transcription is a string
        self.assertIsInstance(transcription, str)

    def test_compare_answers(self):
        user_answer = "This is a sample answer."
        expected_answer = "This is a sample answer."
        # Call the function
        similarity = self.nlp_pipeline.compare_answers(user_answer, expected_answer)
        # Assert the similarity score is not None
        self.assertIsNotNone(similarity)
        # Assert the similarity score is a float
        self.assertIsInstance(similarity, float)
        # Assert the similarity score is 1.0
        self.assertEqual(similarity, 1.0)

if __name__ == '__main__':
    unittest.main()