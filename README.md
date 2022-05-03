# WIFI-RTLS
This project serves as a simple WIFI-RTLS sytem which is intended to be used in conjuction with a Raspberry Pi array. The system uses [Scapy](https://scapy.net/) in order to sniff 802.11 probe requests over a network. The sniffed packets are then sent to a host machine via MQTT so that calculations regarding the probe requests sniffed by each Pi can be performed. Kali-linux with the R4ason kernel is used on each Raspberry Pi within the array, as the R4ason kernel comes with the [Nexmon](https://github.com/seemoo-lab/nexmon) firmware patch which enables the Raspberry Pi's to enter monitor mode.

### Modes
This project's codebase can be seperated into three different sections: passive sniffing, calibration, and trilateration.
