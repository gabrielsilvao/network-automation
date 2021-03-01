import json
from napalm import get_network_driver

routers = ['192.168.3.182','192.168.3.212']

for rt in routers:
    print("Connecting to " + str(rt))
    driver = get_network_driver('ios')
    iosv_router = driver(rt, 'admin', 'cisco')
    iosv_router.open()
    iosv_router.load_merge_candidate(filename='Configuration.txt')
    diffs = iosv_router.compare_config()
    if len(diffs) > 0:
        print(diffs)
        iosv_router.commit_config()
    else:
        print("No changes required.")
        iosv_router.discard_config()
    
iosv_router.close()