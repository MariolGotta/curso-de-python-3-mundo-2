# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo
# desconsiderando os espaços
# Ex: Apos a sopa

frase = str(input('Digite a sua frase: ')).strip().upper()
frase = frase.strip()
palavras = frase.split()
junto = ''.join(palavras)

inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]

print(junto, inverso)
if inverso == junto:
    print('Temos um palíndromo')
else:
    print('Não temos um palíndromo')
