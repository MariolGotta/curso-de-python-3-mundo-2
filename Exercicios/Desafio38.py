# Escreva um programa que leia dois numeros inteiros e compare-os mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Os dois valores são iguais, não há valor maior

valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('Digite o segundo valor: '))

if valor1 > valor2:
    print('O primeiro número é maior, pois {:.2f} é maior que {:.2f}'.format(
        valor1, valor2))

elif valor2 > valor1:
    print('O segundo número é maior, pois {:.2f} é maior que {:.2f}'.format(
        valor2, valor1))

else:
    print('Os dois números são iguais, pois {:.2f} é igual a {:.2f}'.format(
        valor1, valor2))
