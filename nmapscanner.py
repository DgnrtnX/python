import nmap

scanner = nmap.PortScanner()

print("Welcome to the port scanner\n<------------------------->")

ip_add = input("Enter the IP address: ")

type(ip_add)

response = input("\nEnter type on Scan\n1.TCP(syn)\n2.UDP\n3.Comprehensive\nEnter your Choice: ")

if response == "1":
    print("doing syn scan")
    print("version: ", scanner.nmap_version())
    scanner.scan(ip_add, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_add].state())
    print("protocols: \n", scanner[ip_add].all_protocols())
    print("Open ports: ", scanner[ip_add]['tcp'].keys())

elif response == "2":
    print("doing comprehensive scan")
    print("version: ", scanner.nmap_version())
    scanner.scan(ip_add, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_add].state())
    print("protocols: \n", scanner[ip_add].all_protocols())
    print("Open ports: ", scanner[ip_add]['udp'].keys())

elif response == "3":
    print("doing udp scan")
    print("version: ", scanner.nmap_version())
    scanner.scan(ip_add, '1-1024', '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_add].state())
    print("protocols: \n", scanner[ip_add].all_protocols())
    print("Open ports: ", scanner[ip_add]['tcp'].keys())

elif response >= "4":
    print("invalid input")