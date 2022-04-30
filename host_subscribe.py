import paho.mqtt.client as mqtt
from probe_request import ProbeRequest
from constants import DELIM, TOPIC, MQTT_HOSTNAME

sniffed_packets = {}

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code: " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(TOPIC)

def unpack_payload(payload: str) -> ProbeRequest:
    unpacked_payload = payload.split(DELIM)
    return ProbeRequest(unpacked_payload)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic + " : " + str(msg.payload))
    probe_request = unpack_payload(str(msg.payload, 'utf-8'))

    if probe_request.mac_address not in sniffed_packets:
        sniffed_packets[probe_request.mac_address] = {probe_request.rpi_node : probe_request}


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_HOSTNAME, 1883, 60)

client.loop_forever()
