from flask import Flask
from flask_socketio import SocketIO
from api import api_bp

app = Flask(__name__)
app.register_blueprint(api_bp, url_prefix='/api')
socketio = SocketIO(app)

@socketio.on('video_data')
def handle_video_data(data):
    # Handle real-time video data
    pass

@socketio.on('audio_data')
def handle_audio_data(data):
    # Handle real-time audio data
    pass

if __name__ == '__main__':
    socketio.run(app, debug=True)