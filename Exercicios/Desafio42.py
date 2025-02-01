# Refaça o desafio 35 dos triangulos acrescentado o recurso de mostrar que tipo de triangulo será formado
# Equilátero - todos os lados são iguais
# Isóceles - dois lados iguais
# Escaleno - todos os lados diferentes

###################### EX 35 ############################
# Crie um programa que leia o comprimento de três retas
# e diga ao usuario se elas formam ou não um triângulo
#########################################################

a = int(input('Digite o comprimeiro da primeira reta: '))
b = int(input('Digite o comprimento da segunda reta:'))
c = int(input('Digite o comprimento da terceira reta: '))

if (a+b) > c and (b+c) > a and (a+c) > b:
    print('É possível formar um triângulo')

    if a == b == c:
        print('O triângulo possui 3 lados iguais, portanto é um triângulo Equilátero')

    elif (a == b or b == c) or (a == b or a == c):
        print('O triângulo possui 2 lados iguais, portanto é um triângulo Isóceles')

    else:
        print('O triângulo não possui lados iguais, portanto é um triângulo Escaleno')

else:
    print('Não é possível formar um triângulo')
