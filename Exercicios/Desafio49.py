# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher
# só que agora utilizando um laço for

x = int(input('Digite um número para ver a tabuada: '))


print('A tabuada de {} é: '.format(x))
for c in range(1, 11, 1):
    a = x * c
    print('{} * {} = {}'.format(x, c, a))
