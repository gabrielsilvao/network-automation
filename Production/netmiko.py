from netmiko import ConnectHandler

ip = 10.10.20.200

r1 = {
    "device_type": "cisco_ios",
    "ip": ip,
    "port": "22",
    "username": "admin",
    "password": "cisco",
    "secret": "cisco"
}

r2 = {
    "device_type": "cisco_ios",
    "ip": ip,
    "port": "2023",
    "username": "admin",
    "password": "cisco",
    "secret": "cisco"
}

r3 = {
    "device_type": "cisco_ios",
    "ip": ip,
    "port": "2024",
    "username": "admin",
    "password": "cisco",
    "secret": "cisco"
}

filial = {
    "device_type": "cisco_ios",
    "ip": ip,
    "port": "2025",
    "username": "admin",
    "password": "cisco",
    "secret": "cisco"
}

matriz = {
    "device_type": "cisco_ios",
    "ip": ip,
    "port": "2026",
    "username": "admin",
    "password": "cisco",
    "secret": "cisco"
}

devices = [r1, r2, r3, filial, matriz]

for dv in devices:
    print('-'*40, "\nConnecting to the device " + dv)
    net_connect = ConnectHandler(**dv)
    net_connect.enable()

    with open('config.txt','r') as config:
        cfg = config.readlines()
    output = net_connect.send_config_set(cfg)
    print(output)

    with open('verify.txt','r') as verify:
        vrf = verify.readlines()
    output = net_connect.send_config_set(vrf)
    print(output)