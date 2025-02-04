# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

menorpeso = 0
maiorpeso = 0
for x in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(x)))
    if x == 1:
        menorpeso = peso
        maiorpeso = peso
    else:
        if peso > maiorpeso:
            maiorpeso = peso
        if peso < menorpeso:
            menorpeso = peso

print('O maior peso digitado foi de {:.1f}Kg'.format(maiorpeso))
print('O menor peso digitado foi de {:.1f}Kg'.format(menorpeso))
