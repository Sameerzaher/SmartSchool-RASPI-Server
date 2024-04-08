# Assuming your service functions are structured for easy import,
# adjust the import path as necessary based on your project structure.
from services.mindolife.iot_devices_service import change_feature_state_service


def test_change_feature_state():
    # Replace '5' and 'true' with valid test values for your application.
    # This is a simple print-based test; consider using assertions for real tests.
    response = change_feature_state_service('5', 'true')
    print(response)


if __name__ == "__main__":
    test_change_feature_state()
