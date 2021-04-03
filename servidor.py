# -*- coding: utf-8 -*-
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
    nome = nome[1:len(nome)-2]
    nomes.append(nome)
    cliente = open(nome+".txt", "w")

# o servidor se conectou com um cliente e comecou a rodar
conexao, ender = servico.accept()
while True:
    count = 0
    resposta = ''
    dataobj = ''
    msg = conexao.recv(1024).decode()
    if not msg:
        continue
    msg = str(msg)
    msgDividida = msg.split('\n')
    if msgDividida[1] not in nomes:
        count = count + 1
        conexao.send(str.encode("550 Address unknown"))

    # verificando se começa com uma data e termina com .
    if not msgDividida[0] == "data" or not msgDividida[len(msgDividida)-2] == '.':
        count = count + 1
        conexao.send(str.encode("500 Syntax error, command unrecognized"))


    # mensagem ok, conexão com o cliente terminada
    if count == 0:
        msg = '\n'.join(msgDividida[2:len(msgDividida)-2]) + '\n\n'
        open(msgDividida[1]+".txt", "a").write(msg)
        conexao.send(str.encode("ok"))
