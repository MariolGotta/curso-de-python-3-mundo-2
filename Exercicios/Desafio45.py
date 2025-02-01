# Crie um programa que faça o computador jogar Jokenpo com você
# Pedra
# Papel
# Tesoura

import random
import time

print('Vamos jogar Jokenpô, escolha pedra, papel ou tesoura')
print('Digite [ 1 ] para escolher PEDRA')
print('Digite [ 2 ] para escolher PAPEL')
print('Digite [ 3 ] para escolher TESOURA')

jogador = int(input('Digite sua escolha: '))
if jogador == 1:
    escolha_jogador = 'PEDRA'
elif jogador == 2:
    escolha_jogador = 'PAPEL'
else:
    escolha_jogador = 'TESOURA'

lista = [1, 2, 3]

computador = random.choice(lista)

if computador == 1:
    escolha_computador = 'PEDRA'
elif computador == 2:
    escolha_computador = 'PAPEL'
else:
    escolha_computador = 'TESOURA'

if jogador != 1 and jogador != 2 and jogador != 3:
    print('Escolha uma opção válida')

else:
    time.sleep(1)
    print('')
    print('JO\nKEN\nPÔ')
    print('')
    time.sleep(1)
    print('='*25)
    print('O jogador jogou: {}'.format(escolha_jogador))
    print('O computador jogou: {}'.format(escolha_computador))
    print('='*25)
    print('')

    if jogador == computador:
        print('Empate')

    elif jogador == 1 and computador == 2:
        print('O computador ganhou, pois PAPEL ganha de PEDRA')

    elif jogador == 1 and computador == 3:
        print('O jogador ganhou pois, PEDRA ganha de TESOURA')

    elif jogador == 2 and computador == 3:
        print('O computador ganhou pois, TESOURA ganha de PAPEL')

    elif jogador == 2 and computador == 1:
        print('O jogador ganhou, pois PAPEL ganha de PEDRA')

    elif jogador == 3 and computador == 1:
        print('O computador ganhou, pois TESOURA ganha de PEDRA')

    elif jogador == 3 and computador == 2:
        print('O jogador ganhou, pois TESOURA ganha de PAPEL')

print('')
