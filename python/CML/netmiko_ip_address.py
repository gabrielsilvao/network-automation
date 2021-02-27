from netmiko import ConnectHandler

csr1000v = {
    "device_type": "cisco_ios",
    "ip": "10.10.20.200",
    "username": "cisco",
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