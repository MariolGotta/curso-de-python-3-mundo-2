# A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria de acordo com a idade:
# Até 9 anos - Mirim
# Até 14 anos - Infantil
# Até 19 anos - Junior
# Até 25 anos - Senior
# Acima - Master

from datetime import date

ano_nascimento = int(input('Qual o ano de nascimento do atleta?: '))

idade = date.today().year - ano_nascimento

if idade > 0 and idade <= 9:
    print('O atleta possui {:.0f} e está na categoria Mirim'.format(idade))

elif idade <= 14:
    print('O atleta possui {:.0f} e está na categoria Infantil'.format(idade))

elif idade <= 19:
    print('O atleta possui {:.0f} e está na categoria Junior'.format(idade))

elif idade <= 25:
    print('O atleta possui {:.0f} e está na categoria Senior'.format(idade))

else:
    print('O atleta possui {:.0f} e está na categoria Master'.format(idade))
