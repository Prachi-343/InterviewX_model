from flask import Blueprint, request, jsonify
from backend.utils.audio_processing import process_audio

audio_bp = Blueprint('audio_bp', __name__)

@audio_bp.route('/audio', methods=['POST'])
def audio_input():
    audio_data = request.files['audio']
    transcription = process_audio(audio_data)
    return jsonify({"transcription": transcription})
