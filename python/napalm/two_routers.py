import json
from napalm import get_network_driver

bgplist = ['192.168.3.182','192.168.3.212']

for ip_address in bgplist:
    print("Connecting to " + str(ip_address))
    driver = get_network_driver('ios')
    iosv_router = driver(ip_address, 'admin', 'cisco')
    iosv_router.open()
    bgp_neighbors = iosv_router.get_facts()
    print(json.dumps(bgp_neighbors, indent=4))
    iosv_router.close()
    