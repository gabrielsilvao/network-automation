import json
from napalm import get_network_driver

# Define os IPs dos dispositivos a serem configurados
routers = ['192.168.3.182','192.168.3.212']

# Cria um loop para que possa ser configurado os dois roteadores um de cada vez
for rt in routers:
    print("Accessing device " + str(rt))
    driver = get_network_driver('ios')
    iosv_router = driver(rt, 'admin', 'cisco')
    iosv_router.open()

# Usa o arquivo ospf.txt para as configuracoes de OSPF
    iosv_router.load_merge_candidate(filename='ospf.txt')
    diffs = iosv_router.compare_config()
    if len(diffs) > 0:
        print(diffs)
        iosv_router.commit_config()
    else:
        print("No OSPF Changed.")
        iosv_router.discard_config()

# Usa o arquivo acl.txt para as configuracoes de ACL
    iosv_router.load_merge_candidate(filename='acl.txt')
    diffs = iosv_router.compare_config()
    if len(diffs) > 0:
        print(diffs)
        iosv_router.commit_config()
    else:
        print("No ACL Changed.")
        iosv_router.discard_config()

iosv_router.close()