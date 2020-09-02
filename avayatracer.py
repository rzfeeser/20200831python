import pyshark

cap = pyshark.FileCapture("avaya.pcap", display_filter="eth.dst == 00:ca:fe:67:32:48 && sip", output_file="avaya_check_these_packets.pcap")

print(cap)
for packet in cap:
    print(packet.highest_layer)

#macAttack = input("What MAC are we searching for? ")

#packetstocheck = []

#for packet in cap:
#    if packet.eth.src == macAttack or packet.eth.dst == macAttack:
#        packetstocheck.append(packet)

#print(packetstocheck)

#print(packetstocheck[0])
