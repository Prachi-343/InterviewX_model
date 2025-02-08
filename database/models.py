from .database import db
from datetime import datetime
from bson.objectid import ObjectId

class User:
    @staticmethod
    def create(username, email):
        user = {
            "username": username,
            "email": email,
            "interviews": []
        }
        result = db.users.insert_one(user)
        return str(result.inserted_id)

    @staticmethod
    def get_by_id(user_id):
        return db.users.find_one({"_id": ObjectId(user_id)})

    @staticmethod
    def update(user_id, data):
        db.users.update_one({"_id": ObjectId(user_id)}, {"$set": data})

    @staticmethod
    def delete(user_id):
        db.users.delete_one({"_id": ObjectId(user_id)})

class InterviewSession:
    @staticmethod
    def create(user_id):
        session = {
            "user_id": ObjectId(user_id),
            "start_time": datetime.utcnow(),
            "end_time": None,
            "questions": [],
            "analysis_results": []
        }
        result = db.interview_sessions.insert_one(session)
        db.users.update_one({"_id": ObjectId(user_id)}, {"$push": {"interviews": result.inserted_id}})
        return str(result.inserted_id)

    @staticmethod
    def get_by_id(session_id):
        return db.interview_sessions.find_one({"_id": ObjectId(session_id)})

    @staticmethod
    def update(session_id, data):
        db.interview_sessions.update_one({"_id": ObjectId(session_id)}, {"$set": data})

    @staticmethod
    def delete(session_id):
        db.interview_sessions.delete_one({"_id": ObjectId(session_id)})

class Question:
    @staticmethod
    def create(session_id, question_text, expected_answer=None):
        question = {
            "session_id": ObjectId(session_id),
            "question_text": question_text,
            "expected_answer": expected_answer
        }
        result = db.questions.insert_one(question)
        db.interview_sessions.update_one({"_id": ObjectId(session_id)}, {"$push": {"questions": result.inserted_id}})
        return str(result.inserted_id)

    @staticmethod
    def get_by_id(question_id):
        return db.questions.find_one({"_id": ObjectId(question_id)})

    @staticmethod
    def update(question_id, data):
        db.questions.update_one({"_id": ObjectId(question_id)}, {"$set": data})

    @staticmethod
    def delete(question_id):
        db.questions.delete_one({"_id": ObjectId(question_id)})

class AnalysisResult:
    @staticmethod
    def create(session_id, question_id, user_answer, similarity_score):
        analysis_result = {
            "session_id": ObjectId(session_id),
            "question_id": ObjectId(question_id),
            "user_answer": user_answer,
            "similarity_score": similarity_score,
            "timestamp": datetime.utcnow()
        }
        result = db.analysis_results.insert_one(analysis_result)
        db.interview_sessions.update_one({"_id": ObjectId(session_id)}, {"$push": {"analysis_results": result.inserted_id}})
        return str(result.inserted_id)

    @staticmethod
    def get_by_id(result_id):
        return db.analysis_results.find_one({"_id": ObjectId(result_id)})

    @staticmethod
    def update(result_id, data):
        db.analysis_results.update_one({"_id": ObjectId(result_id)}, {"$set": data})

    @staticmethod
    def delete(result_id):
        db.analysis_results.delete_one({"_id": ObjectId(result_id)})