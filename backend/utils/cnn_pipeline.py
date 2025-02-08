import cv2
from models.mtcnn_model import MTCNNModel
from models.facenet_model import FaceNetModel

class CNNPipeline:
    def __init__(self, mtcnn_model_path, facenet_model_path):
        self.mtcnn = MTCNNModel()
        self.facenet = FaceNetModel(facenet_model_path)

    def detect_faces(self, image):
        bounding_boxes, keypoints = self.mtcnn.detect_faces(image)
        return bounding_boxes, keypoints

    def draw_bounding_boxes(self, image, bounding_boxes):
        for box in bounding_boxes:
            x, y, width, height = box
            cv2.rectangle(image, (x, y), (x + width, y + height), (0, 255, 0), 2)
        return image

    def generate_embeddings(self, face_pixels):
        return self.facenet.get_embedding(face_pixels)

    def compare_embeddings(self, emb1, emb2, threshold=0.5):
        return self.facenet.compare_embeddings(emb1, emb2, threshold)

    def process_video(self, video_path):
        cap = cv2.VideoCapture(video_path)
        frames = []
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            bounding_boxes, _ = self.detect_faces(frame)
            frames.append((frame, bounding_boxes))
        cap.release()
        return frames