import paho.mqtt.client as mqtt

TOPIC = 'uark/csce5013/hjnauman/wifi_rtls'
DELIM = ' | '
MQTT_HOSTNAME = 'broker.hivemq.com'
distance_measurements = []

def write_distance_rssi_mean():
    distance = distance_measurements[0].split(DELIM)[0]

    total_rssi = 0
    for i in distance_measurements:
        total_rssi += i.split(DELIM)[1]

    mean_rssi = int(total_rssi / 20)
    print(f'RSSI mean at {distance} feet : {mean_rssi}')

    distance_measurements = []

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code: " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(TOPIC)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic + " : " + str(msg.payload))
    distance_measurements.append(str(msg.payload, 'utf-8'))
    if len(distance_measurements) == 20:
        write_distance_rssi_mean()


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_HOSTNAME, 1883, 60)

client.loop_forever()
