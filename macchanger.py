import re
from random import choice, randint
import subprocess

def random_mac():
    cisco = ["00", "40", "96"]
    dell = ["00", "14", "22"]
    mac_add = choice([cisco,dell])
    for i in range(3):
        one = choice(str(randint(0,9)))
        two = choice(str(randint(0,9)))
        three = str(one+two)
        mac_add.append(three)
    return ":".join(mac_add)

def mac_change(connector, new_mac_address):
    subprocess.call(["ifconfig " + str(connector) + " down"], shell=True)
    subprocess.call(["ifconfig " + str(connector) + " hw ether " + str(new_mac_address) + ' '] ,shell=True)
    subprocess.call(["ifconfig " + str(connector) + " up"], shell=True)

def current_mac_address(connector):
    current = subprocess.check_output(["ifconfig " + str(connector)], shell=True)
    current_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(current))
    print("Old mac address is : {}".format(current_mac))

print('Enter the mac\n1.Manually\n2.automatically\n')
ch = input()
connector = input('Enter the interface: ').strip()
current_mac_address(connector)
if ch == '1':
   new_mac_address = input('Enter the new mac address').strip()
   mac_change(connector, new_mac_address)
elif ch == '2':
   ran_mac_address = random_mac()
   print(ran_mac_address)
   mac_change(connector, ran_mac_address)
else:
    print("Wrong Choice.")
