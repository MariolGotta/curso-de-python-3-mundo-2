# Refaça o exercício 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão aritimética usando a estrutura while


a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))

loop = 10
while loop != 0:
    r10 = a1 + (10 - loop) * r
    loop -= 1
    print(r10, end=' → ')
print('ACABOU')
