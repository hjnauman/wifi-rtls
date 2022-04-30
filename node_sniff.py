from scapy.all import sniff
from scapy.layers.dot11 import Dot11, RadioTap
from scapy.packet import Packet
import paho.mqtt.publish as publish
import datetime
import netaddr

topic = 'uark/csce5013/hjnauman/wifi_rtls'
delim = ' | '

def pkt_handler(pkt: Packet):
    if pkt.haslayer(Dot11) and pkt.haslayer(RadioTap):
        # We are looking for management frames with a probe subtype
        # if neither match we are done here
        if pkt.type != 0 or pkt.subtype != 0x04:
            return

        time_sniffed = datetime.time()
        # time_sniffed = datetime.now().isoformat()
        mac_address = pkt.addr2

        # Parse mac address and look up the organization from the vendor octets
        try:
            parsed_mac = netaddr.EUI(pkt.addr2)
            organization = parsed_mac.oui.registration().org
        except(netaddr.core.NotRegisteredError, e):
            organization = 'UNKNOWN'

        rssi_val = pkt[RadioTap].dBm_AntSignal

        payload = f'{time_sniffed}{delim}{mac_address}{delim}{organization}{delim}{rssi_val}'
        print(payload)

        publish.single(topic, payload, hostname='broker.hivemq.com', port=1883, keepalive=60)

sniff(iface='mon0', prn=pkt_handler)


