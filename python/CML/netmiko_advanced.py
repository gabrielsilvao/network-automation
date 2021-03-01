from netmiko import ConnectHandler

with open('devices.txt','r') as ip_list:
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

        with open('config.txt','r') as config_lines:
            config = config_lines.readlines()
        output = net_connect.send_config_set(config)
        print(output)

        with open('verify.txt','r') as verify_lines:
            verify = verify_lines.readlines()
        output = net_connect.send_config_set(verify)
        print(output)