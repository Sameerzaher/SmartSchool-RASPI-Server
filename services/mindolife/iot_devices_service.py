import logging
import requests

# Configure logging to include file handling (if needed)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler("app.log"), logging.StreamHandler()])


def fetch_iot_devices_data():
    """Fetch IoT devices data from an API."""
    params = {
        'developerKey': 'dec4695bf4450e3a4e0aa2b3f92929b631055ee78b77c5da59d434dee088f1cc',
        'dataType': 'json',
        'client': 'web',
        'jsonResponse': True,
        'getFullData': True,
        'daysOfHistory': 30,
        'sessionKey': '3c387806e55743f337bd915199ea7a8a426f617414ebdd8e736f2d969bb7350a3b14aafb3542940d865eaf72046ef99e78a28e7a1f4dc4eed1490380ed7d391677413bf666ba5ee7f1695dff2f5c692997d99b99765a43ed70c2125253d0aa3b5efe849bf4bafb67f45083f1a1bba0c5d8fef74415fddd9c1030a15e3e2ca689'
    }
    try:
        response = requests.get('https://api.mindolife.com/API/Gateway/getIoTDevices', params=params)
        response.raise_for_status()
        data = response.json()

        # Print full data in the development environment only
        print("Complete API Response Data:", data)  # Use print for immediate console output

        logging.debug("API Response Data: [REDACTED]")  # Log redacted information for security
        if 'devices' not in data:
            logging.error("No devices found in fetched data")
            data['devices'] = []  # Ensure 'devices' key exists
        return data
    except requests.RequestException as e:
        logging.error(f"Error fetching IoT devices: {e}, Response: {response.text if 'response' in locals() else 'No response'}")
        raise

# def fetch_iot_devices_data():
#     """Fetch IoT devices data from an API."""
#     params = {
#         'developerKey': 'dec4695bf4450e3a4e0aa2b3f92929b631055ee78b77c5da59d434dee088f1cc',
#         'dataType': 'json',
#         'client': 'web',
#         'jsonResponse': True,
#         'getFullData': True,
#         'daysOfHistory': 30,
#         'sessionKey': '3c387806e55743f337bd915199ea7a8a426f617414ebdd8e736f2d969bb7350a3b14aafb3542940d865eaf72046ef99e78a28e7a1f4dc4eed1490380ed7d391677413bf666ba5ee7f1695dff2f5c692997d99b99765a43ed70c2125253d0aa3b5efe849bf4bafb67f45083f1a1bba0c5d8fef74415fddd9c1030a15e3e2ca689'
#     }
#     try:
#         response = requests.get('https://api.mindolife.com/API/Gateway/getIoTDevices', params=params)
#         response.raise_for_status()
#         data = response.json()
#         logging.debug(f"Complete API Response Data: {data}")
#         if 'devices' not in data:
#             logging.error(f"No devices found in fetched data: {data}")
#             data['devices'] = []  # Ensure 'devices' key exists
#         return data
#     except requests.RequestException as e:
#         logging.error(f"Error fetching IoT devices: {e}, Response: {response.text if 'response' in locals() else 'No response'}")
#         raise

def transform_iot_devices_data(fetched_data):
    """Transform fetched IoT devices data."""
    transformed_devices = []
    if not fetched_data or 'devices' not in fetched_data:
        logging.error(f"No devices found in fetched data or missing 'devices' key: {fetched_data}")
        return transformed_devices

    for device in fetched_data['devices']:
        iot_device_id = device.get('id', 'Unknown ID')
        features = device.get('features', {})
        for feature_key, feature in features.items():
            try:
                feature_set_id, feature_id = feature_key.split('.')[:2]
                transformed_devices.append({
                    'iotDeviceID': iot_device_id,
                    'featureID': feature_id,
                    'featureSetID': feature_set_id,
                    'featureValue': feature.get('value'),
                    'featureName': feature.get('name'),
                    'featureState': feature.get('state'),
                    'featureSetDefinitionKey': feature.get('featureSetDefinitionKey', 'Unknown Definition Key'),
                    'definitionKey': feature.get('definitionKey', 'Unknown Key'),
                })
            except ValueError as e:
                logging.error(f"Error processing feature key '{feature_key}': {e}")

    logging.debug(f"Transformed Data: {transformed_devices}")
    return transformed_devices

def change_feature_state_service(device_id, state):
    """Change the state of an IoT device."""
    base_url = 'https://api.mindolife.com/API/Gateway/changeFeatureValue'
    headers = {'Content-Type': 'application/json'}
    data = {
        'developerKey': 'dec4695bf4450e3a4e0aa2b3f92929b631055ee78b77c5da59d434dee088f1cc',
        'dataType': 'json',
        'client': 'web',
        'jsonResponse': 'true',
        'iotDeviceID': device_id,
        'featureSetID': '1',
        'featureID': '1',
        'value': {"value": state},
        'sessionKey': '3c387806e55743f337bd915199ea7a8a426f617414ebdd8e736f2d969bb7350a3b14aafb3542940d865eaf72046ef99e78a28e7a1f4dc4eed1490380ed7d391677413bf666ba5ee7f1695dff2f5c692997d99b99765a43ed70c2125253d0aa3b5efe849bf4bafb67f45083f1a1bba0c5d8fef74415fddd9c1030a15e3e2ca689'
    }
    try:
        response = requests.post(base_url, headers=headers, json=data)
        response.raise_for_status()
        
        if 'application/json' in response.headers.get('Content-Type', '').lower():
            return response.json()
        else:
            logging.info("Unexpected Content-Type or no JSON response.")
            return {"message": "Received non-JSON response", "status_code": response.status_code}
    except requests.HTTPError as e:
        logging.error("HTTP Error %s: %s", e.response.status_code, e.response.text)
        raise
    except requests.RequestException as e:
        logging.error("Error changing feature state for device ID %s: %s", device_id, e)
        raise





# import logging

# import requests

# # Configure logging
# logging.basicConfig(level=logging.DEBUG)


# def fetch_iot_devices_data():
#     try:
#         params = {
#             'developerKey': 'dec4695bf4450e3a4e0aa2b3f92929b631055ee78b77c5da59d434dee088f1cc',
#             'dataType': 'json',
#             'client': 'web',
#             'jsonResponse': True,
#             'getFullData': True,
#             'daysOfHistory': 30,
#             'sessionKey': '3c387806e55743f337bd915199ea7a8a426f617414ebdd8e736f2d969bb7350a3b14aafb3542940d865eaf72046ef99e78a28e7a1f4dc4eed1490380ed7d391677413bf666ba5ee7f1695dff2f5c692997d99b99765a43ed70c2125253d0aa3b5efe849bf4bafb67f45083f1a1bba0c5d8fef74415fddd9c1030a15e3e2ca689 '
#         }
#         response = requests.get('https://api.mindolife.com/API/Gateway/getIoTDevices', params=params)
#         response.raise_for_status()
#         return response.json()
#     except requests.RequestException as e:
#         logging.error(f"Error fetching IoT devices: {e}")
#         raise


# def transform_iot_devices_data(fetched_data):
#     transformed_devices = []
#     try:
#         for device in fetched_data.get('devices', []):
#             iot_device_id = device.get('id')
#             features = device.get('features', {})
#             for feature_key, feature in features.items():
#                 # Split the feature key to get featureSetID and featureID
#                 feature_set_id, feature_id = feature_key.split('.')[:2]
#                 transformed_devices.append({
#                     'iotDeviceID': iot_device_id,
#                     'featureID': feature_id,
#                     'featureSetID': feature_set_id,
#                     'featureValue': feature.get('value'),
#                     'featureName': feature.get('name'),
#                     'featureState': feature.get('state'),
#                     'featureSetDefinitionKey': feature.get('featureSetDefinitionKey'),
#                     'definitionKey': feature.get('definitionKey'),
#                 })
#     except Exception as e:
#         logging.exception("Error transforming IoT devices data: %s", e)
#         raise
#     return transformed_devices


# def fetch_and_transform_iot_data():
#     fetched_data = fetch_iot_devices_data()
#     if fetched_data is None:
#         return []
#     transformed_data = transform_iot_devices_data(fetched_data)
#     return transformed_data
# def change_feature_state_service(device_id, state):
#     """Change the state of an IoT device."""
#     base_url = 'https://api.mindolife.com/API/Gateway/changeFeatureValue'
#     headers = {'Content-Type': 'application/json'}
#     data = {
#         'developerKey': 'dec4695bf4450e3a4e0aa2b3f92929b631055ee78b77c5da59d434dee088f1cc',
#         'dataType': 'json',
#         'client': 'web',
#         'jsonResponse': 'true',
#         'iotDeviceID': device_id,
#         'featureSetID': '1',
#         'featureID': '1',
#         'value': {"value": state},
#         'sessionKey': '3c387806e55743f337bd915199ea7a8a426f617414ebdd8e736f2d969bb7350a3b14aafb3542940d865eaf72046ef99e78a28e7a1f4dc4eed1490380ed7d391677413bf666ba5ee7f1695dff2f5c692997d99b99765a43ed70c2125253d0aa3b5efe849bf4bafb67f45083f1a1bba0c5d8fef74415fddd9c1030a15e3e2ca689'
#     }
#     try:
#         response = requests.post(base_url, headers=headers, json=data)
#         response.raise_for_status()
        
#         if 'application/json' in response.headers.get('Content-Type', '').lower():
#             return response.json()
#         else:
#             logging.info("Unexpected Content-Type or no JSON response.")
#             return {"message": "Received non-JSON response", "status_code": response.status_code}
#     except requests.HTTPError as e:
#         logging.error("HTTP Error %s: %s", e.response.status_code, e.response.text)
#         raise
#     except requests.RequestException as e:
#         logging.error("Error changing feature state for device ID %s: %s", device_id, e)
#         raise


