from flask import Blueprint

api_bp = Blueprint('api', __name__)

from . import audio_api, data_api, camera_api