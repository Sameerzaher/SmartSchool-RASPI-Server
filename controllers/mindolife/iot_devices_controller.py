import logging
from flask import Blueprint, jsonify, request
from services.mindolife.iot_devices_service import fetch_iot_devices_data, change_feature_state_service

# Configure detailed logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler("iot_devices.log"), logging.StreamHandler()])

# Define the blueprint for IoT devices
iot_devices_blueprint = Blueprint('iot_devices', __name__)

@iot_devices_blueprint.route('/get_devices', methods=['GET'])
def get_devices():
    try:
        result = fetch_iot_devices_data()
        if isinstance(result, dict) and not result.get('success', True):
            # If result is a dictionary and has a 'success' key that indicates failure
            return jsonify(result), 500
        
        # If result is a list or a successful dict without 'success' key, transform and return
       # Debug print to confirm what's being transformed
        return jsonify(success=True, devices=result)  # Make sure to return 'devices' after transformation
    except Exception as e:
        logging.error("Exception during fetching or transforming IoT devices data: %s", str(e))
        return jsonify(success=False, message='Failed to fetch or transform IoT device data', error=str(e)), 500

@iot_devices_blueprint.route('/change_feature_state', methods=['POST'])
def change_feature_state():
    try:
        data = request.get_json()
        device_id = data['deviceId']
        state = data['state']
        response_data = change_feature_state_service(device_id, state)
        if not response_data['success']:
            return jsonify(response_data), 500
        return jsonify(response_data)
    except Exception as e:
        logging.error("Failed to change feature state: %s", str(e))
        return jsonify(success=False, message='Failed to change feature state', error=str(e)), 500


# import logging
# from flask import Blueprint, jsonify, request

# # Import the IoT devices services module
# from services.mindolife.iot_devices_service import fetch_iot_devices_data, transform_iot_devices_data, change_feature_state_service

# # Configure detailed logging
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# # Define the blueprint for IoT devices
# iot_devices_blueprint = Blueprint('iot_devices', __name__)


# @iot_devices_blueprint.route('/get_devices', methods=['GET'])
# def get_devices():
#     """Endpoint to fetch and display IoT devices."""
#     try:
#         result = fetch_iot_devices_data()
#         if 'success' in result and not result['success']:
#             return jsonify(result), 500
#         devices = transform_iot_devices_data(result)
#         return jsonify(success=True, devices=devices)
#     except Exception as e:
#         logging.error("Failed to fetch or transform IoT devices data: %s", str(e))
#         return jsonify(success=False, message='Failed to fetch or transform IoT device data', error=str(e)), 500


# @iot_devices_blueprint.route('/fetch_and_transform', methods=['GET'])
# def get_iot_devices_data():
#     """Endpoint to fetch and transform IoT devices data."""
#     try:
#         fetched_data = fetch_iot_devices_data()
#         transformed_data = transform_iot_devices_data(fetched_data)
#         return jsonify(transformed_data)
#     except Exception as e:
#         logging.error("Failed to fetch or transform IoT devices data: %s", str(e), exc_info=True)
#         return jsonify(success=False, message='Failed to fetch or transform IoT device data', error=str(e)), 500

# def extract_iot_devices():
#     try:
#         fetched_data = fetch_iot_devices_data()
#         logging.debug(f"Fetched Data: {fetched_data}")  # Ensure this logs enough detail
#         devices = transform_iot_devices_data(fetched_data)
#         logging.debug(f"Transformed Devices: {devices}")  # Log transformed data
#         return jsonify(success=True, devices=devices)
#     except Exception as e:
#         logging.error("Exception occurred while extracting IoT devices: %s", str(e), exc_info=True)
#         return jsonify(success=False, message='Failed to extract IoT device details', error=str(e)), 500

# @iot_devices_blueprint.route('/change_feature_state', methods=['POST'])
# def change_feature_state():
#     try:
#         data = request.get_json()
#         logging.debug(f"Received change request data: {data}")
#         device_id = data['deviceId']
#         state = data['state']
#         response_data = change_feature_state_service(device_id, state)
#         return jsonify(response_data)
#     except Exception as e:
#         logging.error("Failed to change feature state: %s", str(e))
#         return jsonify(success=False, message='Failed to change feature state', error=str(e)), 500




# from flask import Blueprint, jsonify, request  # Use Flask's request

# from services.mindolife.iot_devices_service import fetch_and_transform_iot_data, change_feature_state_service

# iot_devices_blueprint = Blueprint('iot_devices', __name__)


# @iot_devices_blueprint.route('/fetch_and_transform', methods=['GET'])
# def get_iot_devices_data():
#     data = fetch_and_transform_iot_data()
#     return jsonify(data)


# # New endpoint for extracting IoT devices
# @iot_devices_blueprint.route('/extract_iot_devices', methods=['GET'])
# def extract_iot_devices():
#     try:
#         devices = fetch_and_transform_iot_data() 
#         print(devices) # Use the existing service function
#         return jsonify(success=True, devices=devices)
#     except Exception as e:
#         # Error handling, returning a 500 status code and an error message
#         return jsonify(success=False, message='Failed to extract IoT device details', error=str(e)), 500


# @iot_devices_blueprint.route('/change_feature_state', methods=['POST'])
# def change_feature_state():
#     try:
#         data = request.get_json()  # Correctly use Flask's request object here
#         device_id = data['deviceId']
#         state = data['state']
#         response_data = change_feature_state_service(device_id, state)
#         return jsonify(response_data)
#     except Exception as e:
#         return jsonify(success=False, message='Failed to change feature state', error=str(e)), 500