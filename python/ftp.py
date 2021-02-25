import ftplib
import os

FTP = ftplib.FTP()
# Define o nivel do log
#FTP.set_debuglevel(7)
FTP.connect('192.168.3.252')
FTP.login('ftpuser','toor')
print(FTP.dir())

print("\nO que deseja fazer?: \n1 - Criar um Diretorio. \n2 - Entrar em um Diretorio. \n3 - Transferir Arquivo")
opc1 = int(input("\nOpcao: "))

if opc1 == 1:
    dir_name = input("Nome do diretorio: ")
    FTP.mkd('/{0}'.format(dir_name))

if opc1 == 2:
    dir_name = input("Nome do diretorio: ")
    FTP.cwd('/{0}'.format(dir_name))
#    print(FTP.dir('/{0}'.format(dir_name)))

if opc1 == 3:
    for root, dirs, files in os.walk("."):
        for filename in files:
            print(filename)
    file_name = input("Nome do Arquivo para transferir: ")
    file_dst_name = input("Destino do Arquivo: ")
    with open('{0}'.format(file_name), 'rb') as f:
        FTP.storbinary('STOR %s' % '{0}'.format(file_name), f)

FTP.sendcmd('ls')

#print("Voce esta no diretorio: ", FTP.pwd())
#print("Conteudo do diretorio: ", FTP.dir())
FTP.quit()
# teste
# hello world