# Faça um programa que mostre a tabuada de vários números, um de cada vez para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo

c = 1
n = 0
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*25)
    if n < 0:
        break
    if n > 0:
        c = 1
        while True:
            if c <= 10:
                print(f'{n} x {c} = {n*c}')
                c += 1
            else:
                break
    print('-'*25)
print('Programa TABUADA encerrado. Volte sempre!!')
