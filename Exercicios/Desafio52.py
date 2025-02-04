# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo

num = int(input('Digite um número para saber se é numero primo ou não: '))

soma = 0

for x in range(1, num+1, 1):
    if num % x == 0:
        print('\033[1;33m {}\033[m'.format(x), end=' ')
        soma += 1

    else:
        print('\033[1;37m {}\033[m'.format(x), end=' ')


if soma == 2:
    print('\nO {} não é um número primo, pois foi divisível {} vezes'.format(num, soma))

else:
    print('\nO {} é um número primo, pois foi divisível {} vezes'.format(num, soma))
