# Escreva um programa que leia um numero n inteiro qualquer e mostre na tela os n primeiros elementos
# de uma sequencia de fibonacci
# Ex: 0 1 1 2 3 5 8
from math import sqrt

n = int(input('Digite o valor do número para saber\nquais são os números anteriores\nque fazem parte da sequencia de fibonacci:'))

stop = 0
F = 0
phi1 = (1+sqrt(5))/2
phi2 = (1-sqrt(5))/2

while stop < n:
    F = ((phi1**stop - phi2**stop) / sqrt(5))
    print('{:.2f}'.format(F), end=' → ')
    stop += 1
print('Fim')
