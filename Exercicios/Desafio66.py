# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999 que é a condição final de parada
# No final mostre quantos números foram digitados e qual foi a soma entre eles (Desconsiderando a flag).


soma = 0
qtd = 0

while True:
    n = float(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    soma += n
    qtd += 1

print(f'A soma dos {qtd} valores digitados é de: {soma:.2f}')
