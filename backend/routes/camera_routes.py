from flask import Blueprint, request, jsonify
from backend.utils.video_processing import process_video

camera_bp = Blueprint('camera_bp', __name__)

@camera_bp.route('/camera', methods=['POST'])
def camera_input():
    video_data = request.files['video']
    processed_video = process_video(video_data)
    return jsonify({"processed_video": processed_video})
