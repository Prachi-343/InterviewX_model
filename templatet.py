import os
from pathlib import Path

package_name = "InterviewX"

list_of_files = [
    ".github/workflows/ci.yml",
    "api/__init__.py",
    "api/audio_api.py",
    "api/data_api.py",
    "api/camera_api.py",
    "backend/__init__.py",
    "backend/app.py",
    "backend/routes/__init__.py",
    "backend/routes/audio_routes.py",
    "backend/routes/data_routes.py",
    "backend/routes/camera_routes.py",
    "backend/utils/__init__.py",
    "backend/utils/audio_processing.py",
    "backend/utils/video_processing.py",
    "backend/utils/nlp_pipeline.py",
    "backend/utils/cnn_pipeline.py",
    "models/__init__.py",
    "models/facenet_model.py",
    "models/mtcnn_model.py",
    "models/google_speech.py",
    "models/gemini_ai.py",
    "database/__init__.py",
    "database/models.py",
    "database/database.py",
    "scripts/setup_env.sh",
    "scripts/start_server.sh",
    "tests/__init__.py",
    "tests/test_audio_processing.py",
    "tests/test_video_processing.py",
    "tests/test_nlp_pipeline.py",
    "tests/test_cnn_pipeline.py",
    ".gitignore",
    "README.md",
    "environment.yml",
    "requirements.txt"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        print(f"{filepath} already exists")