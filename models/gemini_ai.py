from difflib import SequenceMatcher

class GeminiAI:
    def __init__(self, expected_answers):
        self.expected_answers = expected_answers

    def compare_answers(self, transcribed_answer, question_id):
        expected_answer = self.expected_answers.get(question_id, "")
        return self.calculate_similarity(transcribed_answer, expected_answer)

    @staticmethod
    def calculate_similarity(answer1, answer2):
        return SequenceMatcher(None, answer1, answer2).ratio()
