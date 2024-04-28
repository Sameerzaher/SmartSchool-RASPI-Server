# # device_manager.py
# from gpiozero import LED, MotionSensor, OutputDevice

# class DeviceManager:
#     def __init__(self, led_pin, relay_pin, pir_pin):
#         self.led = LED(led_pin)
#         self.relay = OutputDevice(relay_pin, active_high=False, initial_value=True)
#         self.pir = MotionSensor(pir_pin)
#         self.led_status = False

#     def led_relay_on(self):
#         self.led.on()
#         self.relay.on()
#         self.led_status = True

#     def led_relay_off(self):
#         self.led.off()
#         self.relay.off()
#         self.led_status = False





from gpiozero import LED, MotionSensor

class DeviceManager:
    def __init__(self, led_pin, pir_pin):
        self.led = LED(led_pin)
        self.pir = MotionSensor(pir_pin)

    def led_on(self):
        self.led.on()

    def led_off(self):
        self.led.off()

    def motion_detected(self):
        return self.pir.motion_detected
