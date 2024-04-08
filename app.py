from flask import Flask

from controllers.mindolife.iot_devices_controller import iot_devices_blueprint

# Removed the import of change_feature_state_service since it's not used here directly.

app = Flask(__name__)

# Register the blueprint
app.register_blueprint(iot_devices_blueprint, url_prefix='/api-mindolife')

if __name__ == '__main__':
    app.run(debug=True)
