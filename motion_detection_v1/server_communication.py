
import requests

class ServerCommunication:
    def __init__(self, server_address, server_port):
        self.server_address = server_address
        self.server_port = server_port

    def send_request_to_node(self, state, room_id, space_id):
        """Send state update request to the Node.js server."""
        url = f"http://{self.server_address}:{self.server_port}/api-sensors/motion-detected"
        payload = {
            "state": state,
            "roomId": room_id,  # Ensure that 'roomId' matches the server's expected parameter
            "spaceId": space_id  # Ensure that 'spaceId' matches the server's expected parameter
        }
        try:
            response = requests.post(url, json=payload, timeout=10)  # Adding a timeout
            print(f"Sent '{state}' to Node.js with response: {response.status_code} - {response.text}")
        except requests.exceptions.RequestException as e:
            print(f"Request to Node.js server failed: {e}")


