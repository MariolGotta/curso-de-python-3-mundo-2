# Crie um programa que leia varios números inteiros pelo teclado. No final
# da execução do programa mostre a média entre todos os valores e qual foi o
# maior e o menor valores lidos. O programa deve perguntar ao usuário
# se ele quer ou não continuar a digitar valores

soma = n1 = maior = menor = tentativa = 0

continuar = 'S'

while continuar == 'S':
    tentativa += 1
    n = int(input('Digite os números:'))
    if tentativa == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    n1 = n
    soma += n
    media = soma / tentativa

    continuar = str(input('Deseja continuar? [S/N] ')).upper()
    if continuar == 'S':
        continuar == 'S'
    elif continuar == 'N':
        continuar == 'N'
    else:
        print('Digite uma opção válida')

print('A média entre os valores digitados foi de {:.2f}\n O maior valor foi {}\n O menor valor foi {}'.format(
    media, maior, menor))
