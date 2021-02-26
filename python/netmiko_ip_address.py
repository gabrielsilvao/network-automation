from netmiko import ConnectHandler

csr1000v = {
    "device_type": "cisco_ios",
    "ip": "192.168.3.182",
    "username": "admin",
    "password": "cisco",
    "secret": "cisco",
}

net_connect = ConnectHandler(**csr1000v)

net_connect.enable()

output = net_connect.send_command("show ip int br")
print(output)

for ip in range (10,51,10):
    config_commands = ["interface loopback" + str(ip), "ip address 10.10." + str(ip) + ".1 255.255.255.255"]
    output = net_connect.send_config_set(config_commands)
    print(output)

output = net_connect.send_command("show ip int br")
print(output)