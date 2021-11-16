from scapy.all import *

conf.sniff_promisc=True

def showPacket(packet):
	data = '%s' %(packet[UDP].payload)
	print(data)

def sniffing(filter):
	sniff(filter = filter, prn = showPacket, count=1, store=0)

if __name__=='__main__':
	filter = 'udp port 5060'
	sniffing(filter)
