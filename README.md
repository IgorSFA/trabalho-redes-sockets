# Trabalho de Redes - Sockets

## Feito por Igor Almeida e William Santos

O trabalho é composto por 3 arquivos principais
- cliente.py: código do cliente
- servidor.py: código do servidor
- clientes: arquivo com os endereços dos usuários

Para executar o programa, é necessário ter o python 3 instalado na máquina e seguir os seguintes passos:

```bash
# em um terminal suba o servidor  com o seguinte comando (com python ou python3, dependendo da versão default da sua máquina)
python servidor.py

# a aplicação perguntará o nome do arquivo de clientes, então basta escrever e dar enter


# com outro terminal aberto, suba o cliente com o seguinte comando (com python ou python3, dependendo da versão default da sua máquina)
python cliente.py

# feito isso, a aplicação perguntará qual o email do destinatário, e então a mensagem

# para finalizar a mensagem, insira uma linha com o caractere '.', como indicado na mensagem da aplicação
```

Para finalizar a aplicação, basta executar o comando ctrl+c no terminal do cliente, assim o servidor continuará de pé esperando novas conexões.

## Observações

Utilizamos a porta `50000` para fazer a comunicação, uma vez que a porta `25` pode estar ocupada na máquina.


O arquivo com os clientes precisa seguir o seguinte modelo:
```
<nome_usuário_1>
<nome_usuário_2>
<nome_usuário_3>
...
<nome_usuário_n>

```
Com a última linha em branco.
