from flask import Blueprint, request, jsonify
from backend.utils.data_processing import process_data

data_bp = Blueprint('data_bp', __name__)

@data_bp.route('/data', methods=['POST'])
def data_input():
    data = request.json
    processed_data = process_data(data)
    return jsonify({"processed_data": processed_data})
