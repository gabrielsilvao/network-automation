from virl2_client import ClientLibrary

url = "https://10.10.20.161"
user = "developer"
password = "C1sco12345"

print("-- > Conectando ao CML")
client = ClientLibrary(url, user, password, ssl_verify=False)

print("-- > Parando todos os labs ativos")
for lab in client.all_labs():
    lab.stop()

lab = client.create_lab("DevNet Lab")

r1 = lab.create_node("Hub_R1", "iosv", 100, 50)
print("-- > Criando Hub_R1")
with open('Configuration/r1_config.txt','r') as r1_config:
    r1.config = r1_config.read()

r2 = lab.create_node("Spoke_R2", "iosv", 0, 100)
print("-- > Criando Spoke_R2")
with open('Configuration/r2_config.txt','r') as r2_config:
    r2.config = r2_config.read()

r3 = lab.create_node("Spoke_R3", "iosv", 0, 0)
print("-- > Criando Spoke_R3")
with open('Configuration/r3_config.txt','r') as r3_config:
    r3.config = r3_config.read()

filial = lab.create_node("Filial", "iosv", -150, 100)
print("-- > Criando Filial")
with open('Configuration/filial_config.txt','r') as filial_config:
    filial.config = filial_config.read()

matriz = lab.create_node("Matriz", "iosv", -150, 0)
print("-- > Criando Matriz")
with open('Configuration/matriz_config.txt','r') as matriz_config:
    matriz.config = matriz_config.read()

outside = lab.create_node("external", "external_connector", -50, 350)
print("-- > Criando external")
outside.config = "bridge0"

print("-- > Conectando os dispositivos")
lab.connect_two_nodes(r1, outside)
lab.connect_two_nodes(r1, r2)
lab.connect_two_nodes(r1, r3)
lab.connect_two_nodes(r2, filial)
lab.connect_two_nodes(r3, matriz)

print("-- > Iniciando Lab!")
lab.start()

for node in lab.nodes():
    print(node, node.state, node.cpu_usage)
    for interface in node.interfaces():
        print(interface, interface.readpackets, interface.writepackets)