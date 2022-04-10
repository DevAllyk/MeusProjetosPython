from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
escolha_usuario = int(input('Qual sua jogada? '))
print('JO')
sleep(0.7)
print('KEN')
sleep(0.7)
print('PO!')
print('-='*15)
print('O Computador jogou {}'.format(itens[computador]))
print('O Desafiante jogou {}'.format(itens[escolha_usuario]))
print('-='*15)
if computador == 0: # Computador Escolheu PEDRA
    if escolha_usuario == 0:
        print('EMPATE!')
    elif escolha_usuario == 1:
        print('O Jogador VENCEU!')
    elif escolha_usuario == 2:
        print('O Computador VENCEU!')
    else:
        print('Jogada INVÁLIDA!')
elif computador == 1: # Computador Escolheu PAPEL
    if escolha_usuario == 0:
        print('O Computador VENCEU!')
    elif escolha_usuario == 1:
        print('EMPATE!')
    elif escolha_usuario == 2:
        print('O Jogador VENCEU!')
    else:
        print('Jogada INVÁLIDA!')
elif computador == 2: # Computador Escolheu TESOURA
    if escolha_usuario == 0:
        print('O Jogador VENCEU!')
    elif escolha_usuario == 1:
        print('O Computador VENCEU!')
    elif escolha_usuario == 2:
        print('Deu EMPATE!')
    else:
        print('Jogada INVÁLIDA!')