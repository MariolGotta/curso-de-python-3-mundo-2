# Faça um programa que calcule a soma entre todos os numeros impares que são
# multiplos de tres e que se encontram no intervalo de 1 até 500

soma = 0
valores = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        soma = soma + n
        valores = valores + 1

print('A soma de todos os {:.0f} solicitados é {:.0f}'.format(valores, soma))
