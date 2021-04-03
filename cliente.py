# -*- coding: utf-8 -*-
import socket

HOST = 'localhost'
PORT = 50000

# se comunicando por TCP
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORT))

def handleMensagem():
    msg = ''
    linha = ''
    while linha != '.':
        linha = input()
        msg += linha + '\n'
    return msg

# cliente digita email q quer mandar
msg = ''
# se estiver ok, conexao com o servidor termina, se não continua a conexão
while True:
    email = input("Digite o nome pra quem voce quer mandar email: ")
    print("Escreva a sua mensagem. Quando quiser terminar, pule uma linha e digite o caractere '.'")
    msg = handleMensagem()
    cliente.send(str.encode("data\n"+ email + "\n" + msg))
    dados = cliente.recv(1024)
    msg = dados.decode()
    print(msg)
