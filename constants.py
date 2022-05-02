TOPIC = 'uark/csce5013/hjnauman/wifi_rtls'
DELIM = ' | '
MQTT_HOSTNAME = 'broker.hivemq.com'

RPI_0_COORDINATES = {'X': 0, 'Y': 0}
RPI_1_COORDINATES = {'X': 272, 'Y': 348}
RPI_2_COORDINATES = {'X': 408, 'Y': 0}


# Calibrate rssi to fit distance by solving for path loss exponent (n) and environment constant (c)
# rssid(d) = -10n log_10(d) - c