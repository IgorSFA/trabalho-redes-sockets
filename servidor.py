# -*- coding: utf-8 -*-
import socket
import datetime


HOST = 'localhost'
PORT = 50002

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
    nome = nome.split("\n")[0]
    nomes.append(nome)
    print(nome)
    cliente = open(nome+".txt", "w")

# o servidor se conectou com um cliente e comecou a rodar
conexao, ender = servico.accept()
with conexao:
    while True:
        count = 0
        resposta = ''
        dataobj = ''
        msg = conexao.recv(1024)
        if not msg:
            continue
        msg = str(msg)
        msgDividida = msg.split()
        print(msg)
        if msgDividida[1] not in nomes:
            count = count + 1
            conexao.send(str.encode("550 Address unknown"))

        # verificando se começa com uma data e termina com .
        if not msg.startswith("b'data") or not msg.endswith(".'"):
            count = count + 1
            conexao.send(str.encode("500 Syntax error, command unrecognized"))


        # mensagem ok, conexão com o cliente terminada
        if count == 0:
            open(msgDividida[1]+".txt", "a").write(msgDividida[2] + "\n")
            conexao.send(str.encode("ok"))
            conexao, ender = servico.accept()
