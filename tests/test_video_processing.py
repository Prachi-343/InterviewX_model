import unittest
from backend.utils.video_processing import process_video

class TestVideoProcessing(unittest.TestCase):
    def test_process_video(self):
        # Mock video data
        video_data = "path/to/video/file"
        # Call the function
        faces = process_video(video_data)
        # Assert the faces list is not None
        self.assertIsNotNone(faces)
        # Assert the faces list is a list
        self.assertIsInstance(faces, list)

if __name__ == '__main__':
    unittest.main()