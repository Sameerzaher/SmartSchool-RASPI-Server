import logging
from flask import Blueprint, jsonify, request

# Import the IoT devices services module
from services.mindolife.iot_devices_service import fetch_iot_devices_data, transform_iot_devices_data, change_feature_state_service

# Configure detailed logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Define the blueprint for IoT devices
iot_devices_blueprint = Blueprint('iot_devices', __name__)

@iot_devices_blueprint.route('/fetch_and_transform', methods=['GET'])
def get_iot_devices_data():
    try:
        fetched_data = fetch_iot_devices_data()  # Fetch data from the API
        #logging.debug(f"Fetched Data: {fetched_data}")
        transformed_data = transform_iot_devices_data(fetched_data)  # Transform the fetched data
        return jsonify(transformed_data)
    except Exception as e:
        logging.error("Failed to fetch or transform IoT devices data: %s", str(e), exc_info=True)
        return jsonify(success=False, message='Failed to fetch or transform IoT device data', error=str(e)), 500

def extract_iot_devices():
    try:
        fetched_data = fetch_iot_devices_data()
        logging.debug(f"Fetched Data: {fetched_data}")  # Ensure this logs enough detail
        devices = transform_iot_devices_data(fetched_data)
        logging.debug(f"Transformed Devices: {devices}")  # Log transformed data
        return jsonify(success=True, devices=devices)
    except Exception as e:
        logging.error("Exception occurred while extracting IoT devices: %s", str(e), exc_info=True)
        return jsonify(success=False, message='Failed to extract IoT device details', error=str(e)), 500

@iot_devices_blueprint.route('/change_feature_state', methods=['POST'])
def change_feature_state():
    try:
        data = request.get_json()
        logging.debug(f"Received change request data: {data}")
        device_id = data['deviceId']
        state = data['state']
        response_data = change_feature_state_service(device_id, state)
        return jsonify(response_data)
    except Exception as e:
        logging.error("Failed to change feature state: %s", str(e))
        return jsonify(success=False, message='Failed to change feature state', error=str(e)), 500
