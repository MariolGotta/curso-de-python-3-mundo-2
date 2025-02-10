# Faça um programa que jogue par ou impar com o computador.
# O jogo será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

print('=-'*25)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*25)

perdeu = False
contagem = 0
while perdeu == False:
    teste = False
    n = int(input('Diga um valor: '))
    computador = randint(0, 10)
    soma = n + computador
    while teste == False:
        escolha_jogador = str(input('Par ou Ímpar? [P/I] ')).upper()
        if escolha_jogador == 'P' or escolha_jogador == 'I':
            teste = True
        else:
            teste = False
            print('Digite P ou I')

    if soma % 2 == 0:
        resultado = 'PAR'
        if escolha_jogador == 'P':
            perdeu = False
        else:
            perdeu = True

    if soma % 2 != 0:
        resultado = 'ÍMPAR'
        if escolha_jogador == 'P':
            perdeu = True
        else:
            perdeu = False
    print(
        f'Você jogou {n} e o computador jogou {computador}. Total de {soma} DEU {resultado}')
    if perdeu == True:
        break
    contagem += 1

print('Você PERDEU!')
print('=-'*25)
print(f'GAME OVER! Você venceu {contagem} vezes')
