"""""
Faça um Programa que peça um número inteiro e determine se ele é par ou ímpar. 
Dica: utilize o operador módulo (resto da divisão).
"""""

numero = 0
numero = int(input("Digite um numero inteiro: "))

if numero % 2== 0:
    print(f"O numero {numero} é par")
else:
    print(f"O numero {numero} é impar")
