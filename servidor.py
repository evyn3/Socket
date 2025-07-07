import socket

print("--------Servidor--------")

localhost = socket.gethostbyname('localhost')
print("O endereço do localhost é:", localhost)

address = input("Digite o endereço IP do servidor : ") or 'localhost'
port = input("Digite a porta lógica do servidor (deixe em branco para porta '10000'): ") or 10000

port = int(port)
server_address = (address, port)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(server_address)
server.listen(1)
print("Aguardando a conexão em %s:%s" % server_address)

connection, client_address = server.accept()
print("Conexão estabelecida com o cliente: %s:%s" % client_address)

try:
    while True:
        data = connection.recv(port)
        print("CLIENTE> %s" % data.decode())

        if data.decode() in ['exit', 'fim', 'sair']:
            break

        message = input("SERVIDOR> ")
        connection.sendall(message.encode())

except Exception as e:
    print("Erro: %s" % e)
finally:
    connection.close()
    server.close()
print("Chat finalizado")