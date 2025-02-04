# Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o

soma = 0
for c in range(1, 7, 1):
    num = int(input('Digite o {}° valor: '.format(c)))
    if num % 2 == 0:
        soma += num
print('Você informou {} números'.format(c))
print('A soma dos números digitados é: {}'.format(soma))
