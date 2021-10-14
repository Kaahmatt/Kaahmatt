
"#Uma companhia resolveu dar um aumento de salário aos seus colaboradores"
#"e lhe contrataram para desenvolver o programa que calculará os reajustes"
# "Faça um programa que recebe o salário de um colaborador e o reajuste seguindo o seguinte critério"
# "baseado no salário atual"

#"a) Salários até R$ 2.800,00 (incluindo): aumento de 20%"
#"b) Salários entre R$ 2.800,00 e R$ 7.000,00: aumento de 15%"
#"c) Salários entre R$ 7.000,00 e R$ 15.000,00: aumento de 10%"
#"d) Salários de R$ 15.000,00 em diante: aumento de 5%""
#"e) Após o aumento ser realizado, informe na tela:"
    #"i.	O salário antes do reajuste;"
    #"ii.	O percentual de aumento aplicado;"
    #"iii.	O valor do aumento;"
    #"iv.	O novo salário, após o aumento."


salario = float(input('Salário do colaborador: '))

if (salario <= 2800):
    percentual = 20
elif (salario <= 7000):
    percentual = 15
elif (salario <= 15000):
    percentual = 10
else:
    percentual = 5

print('Salário original: R$ ', salario)
print('Percentual: ', percentual, '%')

percentual = percentual/100.0
aumento = percentual * salario
novo_salario = salario + aumento

print('Aumento: R$ ', aumento)
print('Novo salario: R$ ', novo_salario)

