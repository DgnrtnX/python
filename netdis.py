import scapy.all as scapy

def scanner(ip):
    request = scapy.ARP(pdst=ip)
    # request.show()
    #request.pdst = ip

    broadcast = scapy.Ether()
    broadcast.dst = 'ff:ff:ff:ff:ff:ff'
    # broadcast.show()

    request_broadcast = broadcast/request
    # request_broadcast.show()

    ans = scapy.srp(request_broadcast, timeout=1)[0]

    for elem in ans:
        print(elem[1].psrc)
        print(elem[1].hwsrc)
        print("-------------------")

scanner("192.168.0.1/24")
