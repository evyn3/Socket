import socket

print("--------Cliente--------")

address = input("Digite o endereço IP do servidor que deseja conectar: ") or 'localhost'
port = input("Digite a porta lógica (ou deixe em branco para 10000): ") or 10000
port = int(port)

server_address = (address, port)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(server_address)

print("A conexão foi estabelecida com o servidor: %s:%s" % server_address)

try:
    print("Digite exit para finalizar o chat!!")
    while True:
        message = input("CLIENTE> ")

        client.sendall(message.encode())
        response = client.recv(port)

        if message in ['exit', 'fim', 'sair']:
            break
        
        print("SERVIDOR> %s" % response.decode())

        
except Exception as e:
    print("Erro: %s" % e)
finally:
    client.close()
print("Chat finalizado")
