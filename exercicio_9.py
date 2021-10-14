import datetime
"""""
Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
"""""

dataEscolhida = input("Digite uma data no formato dd/mm/aaaa: ")

#converte string para data no formato dia/mes/ano - y minusculo ano com 2 digitos, maiusculo com 4
try:
   datetime.datetime.strptime(dataEscolhida, "%d/%m/%Y")
except ValueError:
    print(f"A data digitada ({dataEscolhida}) é inválida")
else:
    print(f"A data digitada ({dataEscolhida}) é válida")


