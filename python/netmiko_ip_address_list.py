from netmiko import ConnectHandler

with open('devices.txt') as ip_list:
    for ip in ip_list:
        devices = {
            "device_type": "cisco_ios",
            "ip": ip,
            "username": "cisco",
            "password": "cisco",
            "secret": "cisco",
        }
        print('-'*40, "\nConnecting to the device ", ip, '\n')


        net_connect = ConnectHandler(**devices)
        net_connect.enable()

        output = net_connect.send_command("show ip int br")
        print(output)

        for ip in range (10,51,10):
            config_commands = ["interface loopback" + str(ip), "ip address 10.10." + str(ip) + ".1 255.255.255.255"]
            output = net_connect.send_config_set(config_commands)
            print(output)

        output = net_connect.send_command("show ip int br")
        print(output)
