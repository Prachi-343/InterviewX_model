from mtcnn.mtcnn import MTCNN

class MTCNNModel:
    def __init__(self):
        self.detector = MTCNN()

    def detect_faces(self, image):
        results = self.detector.detect_faces(image)
        bounding_boxes = [result['box'] for result in results]
        keypoints = [result['keypoints'] for result in results]
        return bounding_boxes, keypoints
