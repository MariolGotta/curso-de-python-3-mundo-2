# Faça um programa que leia um número qualquer e mostre seu fatorial
# Ex 5! = 5*4*3*2*1 = 120


n1 = n = int(input('Digite um número para saber seu fatorial: '))

resultado = 1
print('Calculando {}! = '.format(n), end='')
while n > 0:
    print('{}'.format(n), end='')
    print(' x ' if n > 1 else ' = ', end='')
    resultado = resultado * (n)
    n -= 1
print('{}'.format(resultado))
