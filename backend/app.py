from flask import Flask, request, jsonify
from flask_socketio import SocketIO
from api import api_bp
from backend.routes.audio_routes import audio_bp
from backend.routes.camera_routes import camera_bp
from backend.routes.data_routes import data_bp
from backend.utils.audio_processing import process_audio
from backend.utils.video_processing import process_video
from backend.utils.data_processing import process_data

app = Flask(__name__)
app.register_blueprint(api_bp, url_prefix='/api')
app.register_blueprint(audio_bp, url_prefix='/api')
app.register_blueprint(camera_bp, url_prefix='/api')
app.register_blueprint(data_bp, url_prefix='/api')
socketio = SocketIO(app)

@app.route('/api/audio', methods=['POST'])
def audio_input():
    audio_data = request.files['audio']
    transcription = process_audio(audio_data)
    return jsonify({"transcription": transcription})

@app.route('/api/data', methods=['POST'])
def data_input():
    data = request.json
    processed_data = process_data(data)
    return jsonify({"processed_data": processed_data})

@app.route('/api/camera', methods=['POST'])
def camera_input():
    video_data = request.files['video']
    processed_video = process_video(video_data)
    return jsonify({"processed_video": processed_video})

@socketio.on('video_data')
def handle_video_data(data):
    # Handle real-time video data
    print("Received video data")
    processed_video = process_video(data)
    socketio.emit('processed_video', {'data': processed_video})

@socketio.on('audio_data')
def handle_audio_data(data):
    # Handle real-time audio data
    print("Received audio data")
    transcription = process_audio(data)
    socketio.emit('transcription', {'transcription': transcription})

if __name__ == '__main__':
    socketio.run(app, debug=True)