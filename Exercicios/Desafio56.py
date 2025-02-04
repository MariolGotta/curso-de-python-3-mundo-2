# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# A média de idade do grupo
# Qual é o nome do homem mais velho
# Quantas mulheres de menos de 20 anos.

somagrupo = 0
hmaior = ''
somamulher = 0
maioridade = 0

for c in range(1, 5):
    print('--'*4 + ' {}ª pessoa '.format(c) + '--'*4)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()

    somagrupo += idade

    if sexo in 'Mm':
        if idade>maioridade:
            maioridade = idade
            hmaior = nome

    elif sexo in 'Ff':
        if idade <= 20:
            somamulher += 1

    else:
        print('Digite uma opção válida')

media = somagrupo / c

print('A média de idade do grupo é de {} anos'.format(media))
print('O nome do Homem mais velho tem {} anos e se chama {}'.format(maioridade,hmaior))
print('Quantidade de mulheres com menos de 20 anos: {}'.format(somamulher))
