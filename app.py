# # # from flask import Flask, render_template
# # # import threading
# # # from dotenv import load_dotenv
# # # import os
# # # import time
# # # from controllers.mindolife.iot_devices_controller import iot_devices_blueprint
# # # from motion_detection_v1.device_manager import DeviceManager
# # # from motion_detection_v1.server_communication import ServerCommunication

# # # load_dotenv()

# # # app = Flask(__name__)

# # # # Environment Variables
# # # NODE_SERVER_ADDRESS = os.getenv('NODE_SERVER_ADDRESS', 'localhost')
# # # NODE_SERVER_PORT = os.getenv('NODE_SERVER_PORT', '3000')

# # # # Hardware setup
# # # LED_PIN = 17
# # # PIR_PIN = 16
# # # ROOM_ID = "61097711-4866"
# # # SPACE_ID = "61097711"


# # # device_manager = DeviceManager(17, 16, 20)  # Example GPIO pins
# # # server_communication = ServerCommunication(NODE_SERVER_ADDRESS, NODE_SERVER_PORT)

# # # # Register the blueprint
# # # app.register_blueprint(iot_devices_blueprint, url_prefix='/api-mindolife')

# # # # Instantiate device manager and server communication


# # # # Use threading.Event for manual control flag
# # # manual_control_flag = threading.Event()

# # # @app.route("/")
# # # def index():
# # #     manual_control = manual_control_flag.is_set()
# # #     return render_template('index.html', manual_control=manual_control)

# # # @app.route("/<action>", methods=['GET', 'POST'])
# # # def action(action):
# # #     if action == "on":
# # #         device_manager.led_relay_on()
# # #         server_communication.send_request_to_node("on")  # Send state update to Node.js server
# # #         manual_control_flag.set()
# # #     elif action == "off":
# # #         device_manager.led_relay_off()
# # #         server_communication.send_request_to_node("off")  # Send state update to Node.js server
# # #         manual_control_flag.clear()
# # #     elif action == "auto":
# # #         manual_control_flag.clear()
# # #     return render_template('index.html', manual_control=manual_control_flag.is_set())



# # # def monitor_pir():
# # #     motion_detected = False
# # #     last_motion_time = None

# # #     while True:
# # #         if device_manager.motion_detected() and not motion_detected:
# # #             motion_detected = True
# # #             device_manager.led_on()
# # #             server_communication.send_request_to_node("on", ROOM_ID, SPACE_ID)
# # #             last_motion_time = time.time()
# # #             print("Motion detected.")

# # #         elif not device_manager.motion_detected() and motion_detected:
# # #             if (time.time() - last_motion_time) > 10:
# # #                 motion_detected = False
# # #                 device_manager.led_off()
# # #                 server_communication.send_request_to_node("off", ROOM_ID, SPACE_ID)
# # #                 print("No motion detected for 10 seconds.")

# # #         time.sleep(1)


# # # if __name__ == '__main__':
# # #     # Start the monitor_pir thread with required arguments including server_communication
# # #     threading.Thread(target=monitor_pir, args=(device_manager, manual_control_flag, server_communication), daemon=True).start()
# # #     app.run(debug=False, host='0.0.0.0', port=5009)


# # # # # from flask import Flask

# # # # # from controllers.mindolife.iot_devices_controller import iot_devices_blueprint

# # # # # # Removed the import of change_feature_state_service since it's not used here directly.

# # # # # app = Flask(__name__)

# # # # # # Register the blueprint
# # # # # app.register_blueprint(iot_devices_blueprint, url_prefix='/api-mindolife')

# # # # # if __name__ == '__main__':
# # # # #   app.run(debug=True, host='0.0.0.0', port=5009)






# # from flask import Flask, render_template
# # import threading
# # from dotenv import load_dotenv
# # import os
# # import time
# # from controllers.mindolife.iot_devices_controller import iot_devices_blueprint
# # from motion_detection_v1.device_manager import DeviceManager
# # from motion_detection_v1.server_communication import ServerCommunication
# # from gpiozero import LED
# # load_dotenv()

# # app = Flask(__name__)

# # # Environment Variables
# # NODE_SERVER_ADDRESS = os.getenv('NODE_SERVER_ADDRESS', 'localhost')
# # NODE_SERVER_PORT = os.getenv('NODE_SERVER_PORT', '3000')

# # # Hardware setup
# # LED_PIN = 17
# # PIR_PIN = 16
# # BLINK_LED_PIN = 26  # New LED pin

# # BLINK_LED_PIN_2 = 19  # New LED pin

# # ROOM_ID = "61097711-4866"
# # SPACE_ID = "61097711"

# # device_manager = DeviceManager(LED_PIN, PIR_PIN)
# # server_communication = ServerCommunication(NODE_SERVER_ADDRESS, NODE_SERVER_PORT)
# # app.register_blueprint(iot_devices_blueprint, url_prefix='/api-mindolife')

# # # Use threading.Event for manual control flag
# # manual_control_flag = threading.Event()
# # # Setup for the blinking LED
# # blink_led = LED(BLINK_LED_PIN)
# # motion_led = LED(BLINK_LED_PIN_2)
# # @app.route("/")
# # def index():
# #     manual_control = manual_control_flag.is_set()
# #     return render_template('index.html', manual_control=manual_control)
# # def blink_led_function():

# #     """Function to blink an LED to indicate the server is running."""
# #     while True:
# #         blink_led.on()
# #         time.sleep(0.5)
# #         blink_led.off()
# #         time.sleep(0.5)



# # def blink_led_function_1():

# #     """Function to blink an LED to indicate the server is running."""
# #     while True:
# #         motion_led.on()
# #         time.sleep(5)
# #         motion_led.off()
# #         time.sleep(5)
# # @app.route("/<action>", methods=['GET', 'POST'])
# # def action(action):
# #     if action == "on":
# #         device_manager.led_relay_on()
# #         server_communication.send_request_to_node("on")  # Send state update to Node.js server
# #         manual_control_flag.set()
# #     elif action == "off":
# #         device_manager.led_relay_off()
# #         server_communication.send_request_to_node("off")  # Send state update to Node.js server
# #         manual_control_flag.clear()
# #     elif action == "auto":
# #         manual_control_flag.clear()
# #     return render_template('index.html', manual_control=manual_control_flag.is_set())



# # def monitor_pir():
# #     motion_detected = False
# #     last_motion_time = None

# #     while True:
# #         if device_manager.motion_detected() and not motion_detected:
# #             motion_detected = True
# #             device_manager.led_on()
# #             blink_led_function_1()
# #             server_communication.send_request_to_node("on", ROOM_ID, SPACE_ID)
# #             blink_led_function_1()
# #             last_motion_time = time.time()
# #             print("Motion detected.")

# #         elif not device_manager.motion_detected() and motion_detected:
# #             if (time.time() - last_motion_time) > 10:
# #                 motion_detected = False
# #                 device_manager.led_off()
               
# #                 server_communication.send_request_to_node("off", ROOM_ID, SPACE_ID)
# #                 print("No motion detected for 10 seconds.")

# #         time.sleep(1)


# # if __name__ == '__main__':
# #     # Start the monitor_pir thread with required arguments including server_communication
# #     threading.Thread(target=monitor_pir, daemon=True).start()
# #     blink_led_function()
# #     app.run(debug=False, host='0.0.0.0', port=5009)



from flask import Flask, render_template
import threading
from dotenv import load_dotenv
import os
import time
from controllers.mindolife.iot_devices_controller import iot_devices_blueprint
from motion_detection_v1.device_manager import DeviceManager
from motion_detection_v1.server_communication import ServerCommunication
from gpiozero import LED

load_dotenv()

app = Flask(__name__)

# Environment Variables
NODE_SERVER_ADDRESS = os.getenv('NODE_SERVER_ADDRESS', 'localhost')
NODE_SERVER_PORT = os.getenv('NODE_SERVER_PORT', '3000')

# Hardware setup
LED_PIN = 17
PIR_PIN = 16
BLINK_LED_PIN = 26  # New LED pin for server running indication
MOTION_LED_PIN = 19  # New LED pin for motion detection indication
ROOM_ID = "61097711-4866"
SPACE_ID = "61097711"

device_manager = DeviceManager(LED_PIN, PIR_PIN)
server_communication = ServerCommunication(NODE_SERVER_ADDRESS, NODE_SERVER_PORT)
app.register_blueprint(iot_devices_blueprint, url_prefix='/api-mindolife')

# Use threading.Event for manual control flag
manual_control_flag = threading.Event()

# Setup for the blinking LEDs
blink_led = LED(BLINK_LED_PIN)
motion_led = LED(MOTION_LED_PIN)


@app.route("/")
def index():
    manual_control = manual_control_flag.is_set()
    return render_template('index.html', manual_control=manual_control)


def blink_led_function():

    """Function to blink an LED to indicate the server is running."""
    while True:
        blink_led.on()
        time.sleep(0.5)
        blink_led.off()
        time.sleep(0.5)


def blink_led_function_1():

    """Function to blink an LED to indicate motion detection."""
    while True:
        motion_led.on()
        time.sleep(5)
        motion_led.off()
        time.sleep(5)


@app.route("/<action>", methods=['GET', 'POST'])
def action(action):
    if action == "on":
        device_manager.led_relay_on()
        server_communication.send_request_to_node("on")  # Send state update to Node.js server
        manual_control_flag.set()
    elif action == "off":
        device_manager.led_relay_off()
        server_communication.send_request_to_node("off")  # Send state update to Node.js server
        manual_control_flag.clear()
    elif action == "auto":
        manual_control_flag.clear()
    return render_template('index.html', manual_control=manual_control_flag.is_set())


def monitor_pir():
    motion_detected = False
    last_motion_time = None

    while True:
        if device_manager.motion_detected() and not motion_detected:
            motion_detected = True
            device_manager.led_on()
           # Blink motion LED
            server_communication.send_request_to_node("on", ROOM_ID, SPACE_ID)
            last_motion_time = time.time()
            print("Motion detected.")

        elif not device_manager.motion_detected() and motion_detected:
            if (time.time() - last_motion_time) > 10:
                motion_detected = False
                device_manager.led_off()

                server_communication.send_request_to_node("off", ROOM_ID, SPACE_ID)
                print("No motion detected for 10 seconds.")

        time.sleep(1)


if __name__ == '__main__':
    # Start the monitor_pir thread with required arguments including server_communication
    threading.Thread(target=monitor_pir, daemon=True).start()
    blink_led_function()  # Start blinking LED for server running indication
    app.run(debug=False, host='0.0.0.0', port=5009)







# from flask import Flask
# import threading
# from dotenv import load_dotenv
# import os
# import time
# from motion_detection_v1.device_manager import DeviceManager
# from motion_detection_v1.server_communication import ServerCommunication

# load_dotenv()

# app = Flask(__name__)

# # Environment Variables
# NODE_SERVER_ADDRESS = os.getenv('NODE_SERVER_ADDRESS', 'localhost')
# NODE_SERVER_PORT = os.getenv('NODE_SERVER_PORT', '3000')

# # Hardware setup
# LED_PIN = 17
# PIR_PIN = 16
# ROOM_ID = "38197016"
# SPACE_ID = "61097711"

# device_manager = DeviceManager(LED_PIN, PIR_PIN)
# server_communication = ServerCommunication(NODE_SERVER_ADDRESS, NODE_SERVER_PORT)

# def monitor_pir():
#     motion_detected = False
#     last_motion_time = None

#     while True:
#         if device_manager.motion_detected() and not motion_detected:
#             motion_detected = True
#             device_manager.led_on()
#             server_communication.send_request_to_node("on", ROOM_ID, SPACE_ID)
#             last_motion_time = time.time()
#             print("Motion detected.")

#         elif not device_manager.motion_detected() and motion_detected:
#             if (time.time() - last_motion_time) > 10:
#                 motion_detected = False
#                 device_manager.led_off()
#                 server_communication.send_request_to_node("off", ROOM_ID, SPACE_ID)
#                 print("No motion detected for 10 seconds.")

#         time.sleep(1)

# if __name__ == '__main__':
#     threading.Thread(target=monitor_pir, daemon=True).start()
#     app.run(debug=False, host='0.0.0.0', port=5009)
