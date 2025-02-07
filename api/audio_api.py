from flask import request, jsonify
from . import api_bp
from backend.utils.audio_processing import process_audio

@api_bp.route('/audio', methods=['POST'])
def audio_input():
    audio_data = request.files['audio']
    transcription = process_audio(audio_data)
    return jsonify({"transcription": transcription})