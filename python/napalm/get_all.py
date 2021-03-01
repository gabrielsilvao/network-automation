import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl2 = driver('192.168.3.182', 'admin', 'cisco')
iosvl2.open()

ios_output = iosvl2.get_arp_table()
print(json.dumps(ios_output, indent=4))

ios_output = iosvl2.ping('google.com')
print(json.dumps(ios_output, indent=4))

#ios_output = iosvl2.get_bgp_neighbors()
#print(json.dumps(ios_output, indent=4))

#ios_output = iosvl2.get_facts()
#print(json.dumps(ios_output, indent=4))

#ios_output = iosvl2.get_interfaces()
#print(json.dumps(ios_output, indent=4))

#ios_output = iosvl2.get_interfaces_counters()
#print(json.dumps(ios_output, indent=4))