from flask import request, jsonify
from . import api_bp
from backend.utils.data_processing import process_data

@api_bp.route('/data', methods=['POST'])
def data_input():
    data = request.json
    processed_data = process_data(data)
    return jsonify({"processed_data": processed_data})