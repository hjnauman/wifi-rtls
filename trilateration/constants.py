TOPIC = 'uark/csce5013/hjnauman/wifi_rtls'
DELIM = ' | '
MQTT_HOSTNAME = 'broker.hivemq.com'

RPI_0_COORDINATES = (0, 0)
RPI_1_COORDINATES = (29, 22)
RPI_2_COORDINATES = (0, 34)


# Calibrate rssi to fit distance by solving for path loss exponent (n) and environment constant (c)
# rssi(d) = -10n log_10(d) - c
# Calculated n and c from calibration logs
ENVIRONMENT_CONSTANT = 15
PATH_LOSS_EXPONENT = 4.902342806927142