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
       
        print('-'*40, "\nConnecting to the device " + ip)
        net_connect = ConnectHandler(**devices)
        net_connect.enable()

# Read lines from configuration file 'config.txt' and send to the target router
        with open("config.txt") as config_lines:
            config = config_lines.read()
        output = net_connect.send_config_set(config)
        print(output)

# Display the interfaces configured
        with open("verify.txt") as verify_lines:
            verify = config_lines.read()
        output = net_connect.send_config_set(verify)
        print(output)

# Old stuff
'''
        output = net_connect.send_command("show ip int br")
        print(output)
'''