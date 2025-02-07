import cv2
from mtcnn.mtcnn import MTCNN

def process_video(video_data):
    # Process video frames
    detector = MTCNN()
    frames = extract_frames(video_data)
    faces = detect_faces(detector, frames)
    return faces

def extract_frames(video_data):
    # Extract frames from video
    video = cv2.VideoCapture(video_data)
    frames = []
    while video.isOpened():
        ret, frame = video.read()
        if not ret:
            break
        frames.append(frame)
    video.release()
    return frames

def detect_faces(detector, frames):
    # Detect faces in frames
    faces = []
    for frame in frames:
        result = detector.detect_faces(frame)
        faces.append(result)
    return faces