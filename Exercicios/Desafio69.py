# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final mostre:
# Quantas pessoas tem mais de 18 anos.
# Quantos homens foram cadastrados.
# Quantas mulheres tem menos de 20 anos.

continuar = True
sexo = 'MF'
maiores = 0
homens = 0
mulheres = 0
while continuar == True:
    print('-'*25)
    print('CADASTRE UMA PESSOA')
    print('-'*25)

    idade = int(input('Idade: '))

    sexo = str(input('Sexo: [M/F] ')).upper()
    while sexo not in 'MF':
        sexo = str(input('Sexo Inválido, digite novamente: [M/F] ')).upper()
    print('-'*25)
    continuar = str(input('Quer continuar? [S/N]')).upper()
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).upper()
    if continuar == 'S':
        continuar = True
    else:
        continuar = False

    if idade >= 18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade <= 20:
        mulheres += 1


print('='*5 + 'FIM DO PROGRAMA' + '='*5)
print(f'Total de pessoas com mais de 18 anos: {maiores}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheres} mulheres com menos de 20 anos')
