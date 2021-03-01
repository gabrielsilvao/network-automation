import getpass
import telnetlib

user = input('Enter your telnet username: ')
password = getpass.getpass()

f = open('devices.txt','r')

for IP in f:
    IP=IP.strip()
    print ('Get running config from Router ' + (IP))
    HOST = IP
    tn = telnetlib.Telnet(HOST)
    try:
        response = tn.read_until("login: ", timeout=120)
    except EOFError as e:
        print("Connection closed: %s" % e)
    if "login: " in response:
        tn.write(user.encode('ascii') + b'\n')
    else:
        tn.read_until(b'Username: ')
        tn.write(user.encode('ascii') + b'\n') 
#    tn.read_until(b'Username: ')
#    tn.write(user.encode('ascii') + b'\n')
    if password:
        tn.read_until(b'Password: ')
        tn.write(password.encode('ascii') + b'\n')  
    tn.write(b"terminal length 0\n")
    tn.write(b"en\n")
    tn.write(b"cisco\n")
    tn.write(b"show run\n")
    tn.write(b'exit\n')

    readoutput = tn.read_all()
    saveoutput = open("router" + HOST, "w")
    saveoutput.write(readoutput.decode('ascii'))
    saveoutput.write("\n")
    saveoutput.close
