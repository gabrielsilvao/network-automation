import json
from napalm import get_network_driver

routers = ['192.168.3.182','192.168.3.212']

for rt in routers:
    print("Connecting to " + str(rt))
    driver = get_network_driver('ios')
    iosv_router = driver(rt, 'admin', 'cisco')
    iosv_router.open()
    iosv_router.load_merge_candidate(filename='Configuration.txt')
    iosv_router.commit_config()
    router = iosv_router.get_facts()
    print(json.dumps(router, indent=4))
    iosv_router.close()