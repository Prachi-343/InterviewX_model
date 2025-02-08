from keras.models import load_model
import numpy as np

class FaceNetModel:
    def __init__(self, model_path):
        self.model = load_model(model_path)

    def get_embedding(self, face_pixels):
        face_pixels = face_pixels.astype('float32')
        mean, std = face_pixels.mean(), face_pixels.std()
        face_pixels = (face_pixels - mean) / std
        samples = np.expand_dims(face_pixels, axis=0)
        yhat = self.model.predict(samples)
        return yhat[0]

    def compare_embeddings(self, emb1, emb2, threshold=0.5):
        distance = np.linalg.norm(emb1 - emb2)
        return distance < threshold
