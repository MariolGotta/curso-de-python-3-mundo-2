# Melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos.

# O programa encerra quando ele mostrar 0 termos

primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} → '.format(termo), end='')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer a mais? '))
print('Progressão finalizada com {} termos mostrados'.format(total))
