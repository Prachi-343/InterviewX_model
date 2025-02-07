# InterviewX

## Project Summary
**Project Name**: InterviewX

**Description**:
InterviewX is a project that replicates a real-life interview environment in a virtual simulator. It includes two models: a website for user interaction and an AI model for analyzing candidates' validity for recruitment.

## Features
- **Audio input** for user's answers.
- **Data input** for questions.
- **Camera input** for continuous video footage.
- **NLP pipeline** for speech transcription and answer matching.
- **CNN pipeline** for facial detection, recognition, and confidence scoring.
- **Real-time communication** using Socket.IO.
- **AI-based feedback generation**.

## Components and Technologies
1. **Frontend**:
   - User Interface for interactions
   - Captures audio and video input
   - Sends data to the backend via APIs and sockets

2. **Backend**:
   - Flask server
   - Handles API requests for audio, question data, and video input
   - Manages database interactions
   - Coordinates NLP and CNN pipelines

3. **NLP Pipeline**:
   - Audio Preprocessing (librosa, pydub)
   - Speech-to-Text (Google Speech-to-Text API)
   - Answer Matching (Gemini AI, Accuracy Evaluation)

4. **CNN Pipeline**:
   - Facial Detection (MTCNN)
   - Facial Recognition (FaceNet/VGGFace)
   - Confidence Scoring

5. **Real-time Communication**:
   - Socket.IO for transmitting video and audio data

6. **Database**:
   - Stores user data, interview sessions, questions, and analysis results

## File Structure
```plaintext
InterviewX/
├── .github/
│   └── workflows/
│       └── ci.yml
├── api/
│   ├── __init__.py
│   ├── audio_api.py
│   ├── data_api.py
│   ├── camera_api.py
├── backend/
│   ├── __init__.py
│   ├── app.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── audio_routes.py
│   │   ├── data_routes.py
│   │   ├── camera_routes.py
│   └── utils/
│       ├── __init__.py
│       ├── audio_processing.py
│       ├── video_processing.py
│       ├── nlp_pipeline.py
│       ├── cnn_pipeline.py
├── models/
│   ├── __init__.py
│   ├── facenet_model.py
│   ├── mtcnn_model.py
│   ├── google_speech.py
│   ├── gemini_ai.py
├── database/
│   ├── __init__.py
│   ├── models.py
│   ├── database.py
├── scripts/
│   ├── setup_env.sh
│   ├── start_server.sh
├── tests/
│   ├── __init__.py
│   ├── test_audio_processing.py
│   ├── test_video_processing.py
│   ├── test_nlp_pipeline.py
│   ├── test_cnn_pipeline.py
├── .gitignore
├── README.md
├── environment.yml
└── requirements.txt
```

## Setup Instructions
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/InterviewX.git
   cd InterviewX
   ```

2. **Set up the conda environment and install dependencies**:
   ```bash
   ./scripts/setup_env.sh
   ```

3. **Start the Flask server**:
   ```bash
   ./scripts/start_server.sh
   ```

## Usage
- Access the website at `http://localhost:5000`
- Use the provided APIs to send audio, data, and video inputs for analysis

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.

## License
This project is licensed under the MIT License.