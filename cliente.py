# -*- coding: utf-8 -*-
import socket

HOST = 'localhost'
PORT = 50000

# se comunicando por TCP
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORT))

# cliente digita email q quer mandar

# se estiver ok, conexao com o servidor termina, se não continua a conexão
while msg != 'ok':
    email = input("Digite o nome pra quem voce quer mandar email: ")
    msg = input("Digite seu email: ")
    cliente.send(str.encode("data "+ email + " " + msg))
    dados = cliente.recv(1024)
    msg = dados.decode()
    print(msg)
cliente.close()