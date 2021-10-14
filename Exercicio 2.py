#exercicio 2
# Faça um Programa que leia três números e mostre o maior e o menor deles.


numero1 = int(input('Primeiro número: '))
numero2 = int(input('Segundo número: '))
numero3 = int(input('Terceiro número: '))

maior = numero1
menor = numero1

if maior < numero2:
	maior = numero2

if maior < numero3:
	maior = numero3

if menor > numero2:
	menor = numero2

if menor > numero3:
	menor = numero3

print ('Maior:  %d ' %maior)
print ('Menor:  %d ' %menor)

