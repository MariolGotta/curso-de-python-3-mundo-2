# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa e o salário do comprador e em quanto tempo ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela nao pode exceder 30% do salário ou então o empréstimo será negado

from math import pow

valor_da_casa = float(input('Qual o valor da casa? R$: '))
salario = float(input('Qual o valor do seu salário? R$: '))
tempo_de_pagamento = int(input('Quantos anos de financiamentoz?: '))

parcela = valor_da_casa / (tempo_de_pagamento * 12)

if parcela < salario * 0.3:
    print('Para pagar uma casa de R${:.2f} em {:.0f} anos a prestação será de R${:.2f}'.format(
        valor_da_casa, tempo_de_pagamento, parcela))
    print('Empréstimo aprovado')
else:
    print('Para pagar uma casa de R${:.2f} em {:.0f} anos a prestação será de R${:.2f}'.format(
        valor_da_casa, tempo_de_pagamento, parcela))
    print('A prestação é de {:.2f} e o valor maximo do pagamento com seu salário é {:.2f}'.format(
        parcela, salario*0.3))
    print('Empréstimo Reprovado')
