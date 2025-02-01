# Escreva um programa que leia um numero inteiro qualquer e peça para o usuário escolher qual sera a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal

numero = int(input('Digite um número: '))

print('Digite 1 para converter o número de decimal para binário')
print('Digite 2 para converter o número de decimal para octal')
print('Digite 3 para converter o número de decimal para hexadecimal')

conversor = int(input('Digite a opção desejada: '))

if conversor == 1:
    binario = bin(numero)
    print('O número digitado foi {:.0f} e seu binário equivalente é '.format(
        numero) + binario[2:])

elif conversor == 2:
    octal = oct(numero)
    print('O número digitado foi {:.0f} e seu octal equivalente é '.format(
        numero) + octal[2:])

elif conversor == 3:
    hexa = hex(numero)
    print('O número digitado foi {:.0f} e seu hexadecimal equivalente é '.format(
        numero) + hex[2:])

else:
    print('Digite uma opção válida')
