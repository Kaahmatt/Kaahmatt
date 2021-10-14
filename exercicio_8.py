"""""
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. 
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
a.	Dicas:
i.	Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
ii.	Triângulo Equilátero: três lados iguais;
iii.	Triângulo Isósceles: quaisquer dois lados iguais;
iv.	Triângulo Escaleno: três lados diferentes;
"""""

ladoA = 0
ladoB = 0
ladoC = 0

ladoA = int(input("Digite o primeiro lado do triangulo: "))
ladoB = int(input("Digite o segundo lado do triangulo: "))
ladoC = int(input("Digite o terceiro lado do triangulo: "))

if ladoA+ladoB > ladoC or ladoA+ladoC > ladoB or ladoB+ladoC > ladoA:
    print("Estes lados formam um triangulo")
    if ladoA==ladoB==ladoC:
        print("Equilatero")
    elif ladoA==ladoB or ladoA==ladoC or ladoB==ladoC:
        print("Isoceles")
    else:
        print("Escaleno")
else:
    print("Estes lados não formam um triangulo")
