#Gama Academy

#Faça um programa para a leitura de duas notas parciais de um aluno.
# O programa deve calcular a média alcançada por aluno

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

media = (nota1 + nota2) / 2

print('Media: ', media)

if media<7.0:
    print('Reprovado')
elif media<10:
    print('Aprovado')
else:
    print('Aprovado com Distinção!')



