# Crie um programa que leia o ano de nascimento de 7 pessoas.
# No final mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores

from datetime import date

maiores = 0
menores = 0
for c in range(1, 8, 1):
    ano = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    idade = date.today().year - ano
    if idade > 21:
        maiores += 1
    else:
        menores += 1
print('Nessa lista há {} pessoas maiores de idade'.format(maiores))
print('Nessa lista há {} pessoas menores de idade'.format(menores))
