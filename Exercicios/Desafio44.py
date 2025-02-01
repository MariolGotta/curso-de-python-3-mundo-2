# Elabora um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento
# A vista dinehiro e cheque - 10% de desconto
# A vista no cartão - 5% de desconto
# Até 2x no cartão - preço normal
# 3x ou mais no cartão - 20% de juros


valor_produto = float(input('Digite o valor do produto: R$'))
print('Selecione a forma de pagamento:')
print(' [ 1 ] A vista no dinheiro ou cheque - 10% de desconto')
print(' [ 2 ] A vista no Cartão - 5% de desconto')
print(' [ 3 ] Parcelado em até 2x no cartão - preço normal')
print(' [ 4 ] Parcelado em 3x ou mais no cartão - 20% de juros')

pagamento = int(input('Digite a opção escolhida: '))

opcao1 = valor_produto * 0.9
desconto1 = valor_produto - opcao1

opcao2 = valor_produto * 0.95
desconto2 = valor_produto - opcao2

opcao3 = valor_produto

opcao4 = valor_produto * 1.2
aumento4 = opcao4 - valor_produto

if pagamento < 1 or pagamento > 4:
    print('Escolha uma opção válida')

else:
    if pagamento == 1:
        print('O desconto será de R${:.2f} e o valor final do produto será de R${:.2f}'.format(
            desconto1, opcao1))

    elif pagamento == 2:
        print('O desconto será de R${:.2f} e o valor final do produto será de R${:.2f}'.format(
            desconto2, opcao2))
    else:
        parcelas = int(input('Qual a quantidade de parcelas?: '))

        if pagamento == 3 and parcelas <= 2:
            valor_parcela = opcao3 / parcelas
            print(
                'O valor do pagamento será R${:.2f}, não haverá desconto e o valor da parcela será de {:.0f}x de {:.2f}'.format(opcao3, parcelas, valor_parcela))

        else:
            valor_parcela = opcao4 / parcelas
            print('O valor do pagamento será de R${:.2f} e haverá um aumento do valor de R${:.2f} e o valor da parcela será de {:.0500f}x de {:.2f}'.format(
                opcao4, aumento4, parcelas, valor_parcela))
