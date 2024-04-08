from flask import Blueprint, jsonify, request  # Use Flask's request

from services.mindolife.iot_devices_service import fetch_and_transform_iot_data, change_feature_state_service

iot_devices_blueprint = Blueprint('iot_devices', __name__)


@iot_devices_blueprint.route('/fetch_and_transform', methods=['GET'])
def get_iot_devices_data():
    data = fetch_and_transform_iot_data()
    return jsonify(data)


# New endpoint for extracting IoT devices
@iot_devices_blueprint.route('/extract_iot_devices', methods=['GET'])
def extract_iot_devices():
    try:
        devices = fetch_and_transform_iot_data()  # Use the existing service function
        return jsonify(success=True, devices=devices)
    except Exception as e:
        # Error handling, returning a 500 status code and an error message
        return jsonify(success=False, message='Failed to extract IoT device details', error=str(e)), 500


@iot_devices_blueprint.route('/change_feature_state', methods=['POST'])
def change_feature_state():
    try:
        data = request.get_json()  # Correctly use Flask's request object here
        device_id = data['deviceId']
        state = data['state']
        response_data = change_feature_state_service(device_id, state)
        return jsonify(response_data)
    except Exception as e:
        return jsonify(success=False, message='Failed to change feature state', error=str(e)), 500
