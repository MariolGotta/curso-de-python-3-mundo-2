# Crie um programa que leia o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar.
# No final mostre:
# Qual é o total gasto na compra.
# Quantos produtos custam mais de R$1000,00.
# Qual é o nome do produto mais barato.
loja = 'LOJA SUPER BARATÃO'
print('-'*25)
print(f'{loja:^20}')
print('-'*25)

continuar = True
quantidade = 0
total = 0
caropreco = baratopreco = preco = cont = 0
baratonome = ' '

while continuar == True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: '))
    continuar = str(input('Quer continuar? [S/N]')).upper().split()[0]
    while continuar not in 'SN':
        continuar = str(
            input('Você digitou errado, quer continuar? [Sim/Nao] ')).upper().split()[0]
    if continuar == 'S':
        continuar = True
    else:
        continuar = False
    print('-'*25)
    if preco >= 1000:
        quantidade += 1
    cont += 1
    if cont == 1 or preco < baratopreco:
        baratopreco = preco
        baratonome = produto
    total += preco

print('-'*25 + 'FIM DO PROGRAMA' + '-'*25)
print(f'O total da compra foi de R${total:.2f}')
print(f'Temos {quantidade:.0f} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {baratonome} que custa R$ {baratopreco:.2f}')
