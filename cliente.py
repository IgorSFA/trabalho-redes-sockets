import socket

HOST = 'localhost'
PORT = 50000

# se comunicando por TCP
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORT))

# cliente digita email q quer mandar
msg = input("Digite o nome pra quem voce quer mandar email: ")
cliente.send(str.encode(msg))

# resposta do servidor
dados = cliente.recv(1024)
msg = dados.decode()

# se estiver ok, conexao com o servidor termina, se não continua a conexão
while msg != 'ok':
    print(msg)
    msg = input("Digite seu email: ")
    cliente.send(str.encode(msg))
    dados = cliente.recv(1024)
    msg = dados.decode()
cliente.close()