import unittest
from backend.utils.cnn_pipeline import CNNPipeline

class TestCNNPipeline(unittest.TestCase):
    def setUp(self):
        self.cnn_pipeline = CNNPipeline()

    def test_detect_faces(self):
        # Mock image data
        image_data = "path/to/image/file"
        # Call the function
        boxes, probs, landmarks = self.cnn_pipeline.detect_faces(image_data)
        # Assert the boxes list is not None
        self.assertIsNotNone(boxes)
        # Assert the boxes list is a list
        self.assertIsInstance(boxes, list)

    def test_generate_embedding(self):
        # Mock image data
        image_data = "path/to/image/file"
        # Call the function
        embedding = self.cnn_pipeline.generate_embedding(image_data)
        # Assert the embedding is not None
        self.assertIsNotNone(embedding)
        # Assert the embedding is a tensor
        self.assertTrue(hasattr(embedding, 'shape'))

    def test_compare_embeddings(self):
        # Mock embeddings
        embedding1 = self.cnn_pipeline.generate_embedding("path/to/image1/file")
        embedding2 = self.cnn_pipeline.generate_embedding("path/to/image2/file")
        # Call the function
        is_same_person = self.cnn_pipeline.compare_embeddings(embedding1, embedding2)
        # Assert the result is a boolean
        self.assertIsInstance(is_same_person, bool)

if __name__ == '__main__':
    unittest.main()