# Crie um programa que leia vários números inteiros pelo teclado
# O programa só vai parar quando o usuário digitar 999, que é a condição de parada
# No final mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o 999)

n = 0
soma = 0
contagem = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    soma += n
    contagem += 1
print('Você digitou {} números e a soma dos números digitados é: {}'.format(
    contagem, soma-999))
