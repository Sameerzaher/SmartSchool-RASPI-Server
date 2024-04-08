import logging

import requests

# Configure logging
logging.basicConfig(level=logging.DEBUG)


def fetch_iot_devices_data():
    try:
        params = {
            'developerKey': 'dec4695bf4450e3a4e0aa2b3f92929b631055ee78b77c5da59d434dee088f1cc',
            'dataType': 'json',
            'client': 'web',
            'jsonResponse': True,
            'getFullData': True,
            'daysOfHistory': 30,
            'sessionKey': '3c387806e55743f337bd915199ea7a8a426f617414ebdd8e736f2d969bb7350a3b14aafb3542940d865eaf72046ef99e78a28e7a1f4dc4eed1490380ed7d391677413bf666ba5ee7f1695dff2f5c692997d99b99765a43ed70c2125253d0aa3b5efe849bf4bafb67f45083f1a1bba0c5d8fef74415fddd9c1030a15e3e2ca689 '
        }
        response = requests.get('https://api.mindolife.com/API/Gateway/getIoTDevices', params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"Error fetching IoT devices: {e}")
        raise


def transform_iot_devices_data(fetched_data):
    transformed_devices = []
    try:
        for device in fetched_data.get('devices', []):
            iot_device_id = device.get('id')
            features = device.get('features', {})
            for feature_key, feature in features.items():
                # Split the feature key to get featureSetID and featureID
                feature_set_id, feature_id = feature_key.split('.')[:2]
                transformed_devices.append({
                    'iotDeviceID': iot_device_id,
                    'featureID': feature_id,
                    'featureSetID': feature_set_id,
                    'featureValue': feature.get('value'),
                    'featureName': feature.get('name'),
                    'featureState': feature.get('state'),
                    'featureSetDefinitionKey': feature.get('featureSetDefinitionKey'),
                    'definitionKey': feature.get('definitionKey'),
                })
    except Exception as e:
        logging.exception("Error transforming IoT devices data: %s", e)
        raise
    return transformed_devices


def fetch_and_transform_iot_data():
    fetched_data = fetch_iot_devices_data()
    if fetched_data is None:
        return []
    transformed_data = transform_iot_devices_data(fetched_data)
    return transformed_data

