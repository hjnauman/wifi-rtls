import paho.mqtt.client as mqtt
from constants import DELIM, TOPIC, MQTT_HOSTNAME, PATH_LOSS_EXPONENT, ENVIRONMENT_CONSTANT
from plot import plot_circles

rpi_estimated_distances = {}
rssi_measurements = []
rpi_node = 0

def calculate_device_distance_from_node(rssi):
    # rssi(d) = -10n log_10(d) - c
    distance = 10**((float(rssi) + ENVIRONMENT_CONSTANT)/(-10.0*PATH_LOSS_EXPONENT))

    return distance

def calculate_mean_rssi(rssi_measurements):
    distance = rssi_measurements[0].split(DELIM)[0]

    total_rssi = 0
    for i in rssi_measurements:
        total_rssi += int(i.split(DELIM)[1])

    mean_rssi = int(total_rssi / 20)

    return mean_rssi

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code: " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(TOPIC)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    global rpi_node
    global rssi_measurements
    global rpi_estimated_distances

    print(msg.topic + " : " + str(msg.payload))
    rssi_measurements.append(str(msg.payload, 'utf-8'))

    if len(rssi_measurements) == 20:
        mean_rssi = calculate_mean_rssi(rssi_measurements)
        estimated_distance = calculate_device_distance_from_node(mean_rssi)
        rpi_estimated_distances[rpi_node] = estimated_distance
        print(f'Mean rssi for rpi_node {rpi_node} : {mean_rssi}')
        print(f'Estimated distance of phone from rpi_node {rpi_node} : {estimated_distance}')
        print()

        rpi_node += 1
        rssi_measurements.clear()

        if rpi_node == 3:
            plot_circles(rpi_estimated_distances[0], rpi_estimated_distances[1], rpi_estimated_distances[2])


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_HOSTNAME, 1883, 60)

client.loop_forever()
