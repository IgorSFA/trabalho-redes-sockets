import socket
import datetime


HOST = 'localhost'
PORT = 50000

# usando TCP para o transporte de mensagens
servico = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servico.bind((HOST, PORT))
servico.listen()
nomes = []

# pegando o nome do arquivo com os nomes dos clientes
arq = input("Digite o caminho do arquivo: ")
arquivo = open(arq, "r")

# criando um arquivo para cada cliente
for x in arquivo:
    nome = x
    nome = nome.split("\n")
    nome = nome[0] + ".txt"
    nomes.append(nome)
    print(nome)
    cliente = open(nome, "w")

# o servidor se conectou com um cliente e começou a rodar
conexao, ender = servico.accept()
while True:
    count = 0
    resposta = ''
    dataobj = ''
    msg = conexao.recv(1024)
    msg = str(msg)
    msgDividida = msg.split()
    print(msg)
    # veridicando se a msg nao é vazia
    if not msg:
        print('Fechando conexão')
        conexao.close()
        break
    # verificando se começa com uma data
    try:
        print(msgDividida[1])
        datetime.datetime.strptime(msgDividida[1], '%Y-%m-%d')
    except ValueError:
        count = 1
        conexao.send(str.encode(" Data errada"))
        # raise ValueError("Data errada")
    # verificando se termina com .
    if not msg.endswith(".'"):
        ba = msg.endswith(".")
        print(ba)
        count = count + 1
        conexao.send(str.encode("Nao terminou com ."))
    # mensagem ok, conexão com o cliente terminada
    if count == 0:
        conexao.send(str.encode("ok"))
        conexao.close()
        break