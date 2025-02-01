
# Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar
# Se é a hora de ele se alistar
# Se ja passou o tempo de alistamento
# Seu programa também deverá mostrar o tempo que falta ou se passou do prazo

from datetime import date

ano_nascimento = int(input('Ano de nascimento: '))

ano_alistamento = ano_nascimento + 18
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
tempo_faltante = ano_alistamento - idade - ano_nascimento
tempo_passado = idade - ano_alistamento + ano_nascimento

if idade < 18:
    print('Ainda faltam {:.0f} anos para você se alistar'.format(
        tempo_faltante))
    print('Seu alistamento será em {:.0f}'.format(ano_alistamento))

elif idade == 18:
    print('Você nasceu em {:.0f} tem {:.0f} anos em {:.0f}'.format(
        ano_nascimento, idade, ano_atual))
    print('Você deve se alistar imediatamente')

else:
    print('Você deveria ter feito o alistamento há {:.0f} anos'.format(
        tempo_passado))
    print('Seu alistamento foi em {:.0f}'.format(ano_alistamento))
