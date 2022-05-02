import netaddr
import paho.mqtt.publish as publish
import sys
from scapy.all import sniff
from scapy.layers.dot11 import Dot11, RadioTap
from scapy.packet import Packet

from constants import DELIM, MQTT_HOSTNAME, TOPIC

transmitter_distance = sys.argv[1]
mqtt_messages_sent = 0

def pkt_handler(pkt: Packet):
    if pkt.haslayer(Dot11) and pkt.haslayer(RadioTap):
        # We are looking for management frames with a probe subtype
        # if neither match we are done here
        if pkt.type != 0 or pkt.subtype != 0x04:
            return

        mac_address = pkt.addr2

        # Check that mac address matches transmission device prior to sending message
        if mac_address == '0a:1d:1a:b6:87:56':
            rssi_val = pkt[RadioTap].dBm_AntSignal
            payload = f'{transmitter_distance}{DELIM}{rssi_val}'
            publish.single(TOPIC, payload, hostname=MQTT_HOSTNAME, port=1883, keepalive=60)
            print(mqtt_messages_sent)

            mqtt_messages_sent += 1
            if mqtt_messages_sent == 20:
                sys.exit(f'Distance calibration complete for {transmitter_distance} feet')

sniff(iface='mon0', prn=pkt_handler)