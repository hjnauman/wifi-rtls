# WIFI-RTLS
This project serves as a simple WIFI-RTLS sytem which is intended to be used in conjuction with a Raspberry Pi array. The system uses [Scapy](https://scapy.net/) in order to sniff 802.11 probe requests over a network. The sniffed packets are then sent to a host machine via MQTT so that calculations regarding the probe requests sniffed by each Pi can be performed. Kali-linux with the R4ason kernel is used on each Raspberry Pi within the array, as the R4ason kernel comes with the [Nexmon](https://github.com/seemoo-lab/nexmon) firmware patch which enables the Raspberry Pi's to enter monitor mode.

### Modes
This project's codebase can be seperated into three different sections: 
- Passive Sniffing
- Calibration
- Trilateration.

### Passive Sniffing
Passive sniffing was the first mode implemented for this project. The main purpose of this mode was to test the capabilities of the Raspberry Pi's. The code for this section can be found in [host_subscribe.py](https://github.com/hjnauman/wifi-rtls/blob/main/host_subscribe.py), [node_sniff.py](https://github.com/hjnauman/wifi-rtls/blob/main/node_sniff.py), [constants.py](https://github.com/hjnauman/wifi-rtls/blob/main/constants.py), and [probe_request.py](https://github.com/hjnauman/wifi-rtls/blob/main/probe_request.py). 

[node_sniff.py](https://github.com/hjnauman/wifi-rtls/blob/main/node_sniff.py) serves as the Raspberry Pi client code. By setting up an interface with monitor mode enabled using the [Nexmon](https://github.com/seemoo-lab/nexmon) patch on the Raspberry Pi, the Raspberry Pi's can sniff probe requrests and send data about the probe request to the host machine over mqtt.

[host_subscribe.py](https://github.com/hjnauman/wifi-rtls/blob/main/host_subscribe.py) then actively listens to the topic being broadcast on in order to capture probe request data from the Raspberry Pi's and store them within a packets sniffed dict. This dict can be used to estimate the number of devices nearby and thus the number of people in the area. 

### Calibration
The main method of determining a devices distance form the Raspberry Pi's is through the use of a Log Normal Shadowing Model who's formula can be represented as:

`RSSI = -10n Log_10(d) - c`

- RSSI = signal strenght of probe request
- n = the path loss exponent
- d = the distance of the probe request from the raspberry pi
- c = the environment constant

[host_rssi_calibration.py](https://github.com/hjnauman/wifi-rtls/blob/main/calibration/host_rssi_calibration.py) is used to listen to 20 probe requests from a known device at a known distance from the Raspberry Pi. Infomration about the probe requests are sent from [node_rssi_calibration.py](https://github.com/hjnauman/wifi-rtls/blob/main/calibration/node_rssi_calibration.py) and are used to calculate a mean RSSI value for multiple different distances. This information is then used within [calibration.py](https://github.com/hjnauman/wifi-rtls/blob/main/calibration/calibration.py) to estimate the features of the Log Normal Shadowing Model. Information about sent packets are stored in the [measurements](https://github.com/hjnauman/wifi-rtls/tree/main/calibration/measurements) directory.

### Trilateration
After calibration had been performed to calculate the features of the Log Normal Shadwoing Model, the model could then be used to show examples of trilateration. Unfortunately for my testing I was only able to get one of three Raspberry Pi's to work with the [Nexmon](https://github.com/seemoo-lab/nexmon) firmware update. Due to this issue the trilateration system was built to use only one Raspberry Pi. [node_rssi_trilateration.py](https://github.com/hjnauman/wifi-rtls/blob/main/trilateration/node_rssi_trilateration.py) is used to sniff packets from a specific device at a known position in the testing area (my apartment). Similarly to the calibration system, 20 packets are sniffed from each Raspberry Pi node position. By using one Raspberry Pi and moving it from different positions within my apartment I could find the mean rssi value of packets being sniffed from those positions. This data is calculated by [host_rssi_trilateration](https://github.com/hjnauman/wifi-rtls/blob/main/trilateration/host_rssi_trilateration.py) such that a distance from each Raspberrry Pi node can be calculated for a signle position of my phone.
