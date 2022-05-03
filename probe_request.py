from typing import List

class ProbeRequest:
    def __init__(self, unpacked_mqtt_payload: List[str]):
        self.rpi_node = int(unpacked_mqtt_payload[0])
        self.time = unpacked_mqtt_payload[1]
        self.mac_address = unpacked_mqtt_payload[2]
        self.ssid = unpacked_mqtt_payload[3]
        self.organization = unpacked_mqtt_payload[4]
        self.rssi = int(unpacked_mqtt_payload[5])



