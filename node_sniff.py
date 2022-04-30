from datetime import datetime

import netaddr
import paho.mqtt.publish as publish
from scapy.all import sniff
from scapy.layers.dot11 import Dot11, RadioTap
from scapy.packet import Packet

from constants import DELIM, MQTT_HOSTNAME, TOPIC

# This variable must be indpendently set for each RPi node in the array
rpi_node = 0

def pkt_handler(pkt: Packet):
    if pkt.haslayer(Dot11) and pkt.haslayer(RadioTap):
        # We are looking for management frames with a probe subtype
        # if neither match we are done here
        if pkt.type != 0 or pkt.subtype != 0x04:
            return

        time_sniffed = datetime.now()
        mac_address = pkt.addr2
        ssid = pkt.info

        # Parse mac address and look up the organization from the vendor octets
        try:
            parsed_mac = netaddr.EUI(pkt.addr2)
            organization = parsed_mac.oui.registration().org
        except:
            organization = 'UNKNOWN'

        rssi_val = pkt[RadioTap].dBm_AntSignal

        payload = f'{rpi_node}{DELIM}{time_sniffed}{DELIM}{mac_address}{DELIM}{ssid}{DELIM}{organization}{DELIM}{rssi_val}'
        print(payload)

        publish.single(TOPIC, payload, hostname=MQTT_HOSTNAME, port=1883, keepalive=60)

sniff(iface='mon0', prn=pkt_handler)


