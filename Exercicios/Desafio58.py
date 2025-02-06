# Melhore o jogo do desafio 28 onde o computador vai "pensar" em um numero de 1 a 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
# foram necessários para vencer.

from random import randint
from time import sleep

n1 = randint(0, 10)
tentativa = 0
acertou = False
print('Sou seu computador')
print('Acabei de pensar em um número de 1 a 10')
print('Será que você consegue adivinhar qual foi?')

while not acertou:
    n = int(input('Digite seu palpite: '))
    print('Processando ...')
    tentativa += 1
    sleep(1)
    if n1 == n:
        acertou = True
    else:
        if n > n1:
            print('Menos... Tente mais uma vez')
        elif n < n1:
            print('Mais... Tente mais uma vez')

print('O número escolhido pelo computador foi {} e foram necessárias {} tentativas do jogador para acertar.'.format(n1, tentativa))
