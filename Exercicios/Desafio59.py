# Crie um programa que leia dois valores e mostre na tela:
# [1] Somar
# [2] Multiplicar
# [3] Maior
# [4] Novos números
# [5] Sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso

from time import sleep

print('Digite dois valores:')
n1 = float(input('Digite o primeiro número:'))
n2 = float(input('Digite o segundo número:'))
print('Qual operação deseja realizar?')
print('[1] Somar')
print('[2] Multiplicar')
print('[3] Maior')
print('[4] Novos números')
print('[5] Sair do programa')

opt = int(input('Qual a opçao desejada?: '))
while opt != 5:
    if opt == 1:
        res = n1 + n2
        print('{:.2f} + {:.2f} = {:.2f}'.format(n1,n2,res))
        opt = int(input('Qual a opçao desejada?: '))
    elif opt == 2:
        res = n1 * n2
        print('{:.2f} * {:.2f} = {:.2f}'.format(n1, n2, res))
        opt = int(input('Qual a opçao desejada?: '))
    elif opt == 3:
        if n1 > n2:
            print('O {:.2f} é maior que {:.2f}'.format(n1, n2))
        else:
            print('O {:.2f} é maior que {:.2f}'.format(n2, n1))
        opt = int(input('Qual a opçao desejada?: '))
    elif opt == 4:
        n1 = float(input('Digite o primeiro número:'))
        n2 = float(input('Digite o segundo número:'))
        print('Qual operação deseja realizar?')
        print('[1] Somar')
        print('[2] Multiplicar')
        print('[3] Maior')
        print('[4] Novos números')
        print('[5] Sair do programa')
        opt = int(input('Qual a opçao desejada?: '))
    else:
        print('Digite uma opção válida')
        print('[1] Somar')
        print('[2] Multiplicar')
        print('[3] Maior')
        print('[4] Novos números')
        print('[5] Sair do programa')
        opt = int(input('Qual a opçao desejada?: '))
        
print('Processando...')
sleep(3)
print('FIM')
