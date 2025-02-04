# Faça um programa e mostre na tela uma contagem regressiva para o estouro de fogos de artificio
# indo de 10 até 0 com uma pausa de 1 segundo entre eles.
import time

num = int(input('Quanto tempo falta para estourar os fogos (s): '))

for c in range(num, -1, -1):
    time.sleep(1)
    print(num)
    num = num - 1

time.sleep(0.5)
print('Os foguetes estouraram!!')
