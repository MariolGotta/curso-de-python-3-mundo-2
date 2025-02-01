# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final de acordo com a média atingida
# Média abaixo de 5.0 Reprovado
# Média entre 5 e 6.9 Recuperação
# Média 7 ou superior Aprovado

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5 and media > 0:
    print('Sua média foi {:.2f}, logo está reprovado'.format(media))

elif media > 5 and media < 7:
    print('Sua média foi {:.2f}, logo está em recuperação'.format(media))

elif media >= 7 and media < 10:
    print('Sua média foi {:.2f}, logo você está aprovado'.format(media))

else:
    print('Insira notas válidas.')
