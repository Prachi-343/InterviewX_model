from flask import request, jsonify
from . import api_bp
from backend.utils.video_processing import process_video

@api_bp.route('/camera', methods=['POST'])
def camera_input():
    video_data = request.files['video']
    processed_video = process_video(video_data)
    return jsonify({"processed_video": processed_video})