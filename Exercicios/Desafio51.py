# Desenvolva um programa que leia o primeiro termo e a razão de uma progressão aritimética.
# No final mostre os 10 primeiros termos dessa progressão

a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
r10 = a1 + (10 - 1) * r

for x in range(a1, r10 + r, r):
    print(x, end=' → ')
print('ACABOU')
