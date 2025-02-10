# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar
# quantas cédulas de cada valor serão entregues
# Obs: Considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10, e R$ 1,00.

banco = 'BANCO CEV'

print('='*25)
print(f'{banco:^25}')
print('='*25)

resto = 0
conta50 = conta20 = conta10 = conta1 = 0

valor = int(input('Qual valor você quer sacar? R$'))

while valor != 0:
    while valor >= 50:
        conta50 += 1
        valor -= 50
    while valor >= 20:
        conta20 += 1
        valor -= 20
    while valor >= 10:
        conta10 += 1
        valor -= 10
    while valor >= 1:
        conta1 += 1
        valor -= 1

print(f'Total de {conta50} cédulas de R$50')
print(f'Total de {conta20} cédulas de R$50')
print(f'Total de {conta10} cédulas de R$50')
print(f'Total de {conta1} cédulas de R$50')
