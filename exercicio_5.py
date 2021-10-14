"""""
# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, 
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 
11% do Salário Bruto, mas não é descontado (é a empresa que deposita). 
O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
a.	Desconto do IR:
i.	Salário Bruto até R$ 2.000,00 (inclusive) - isento
ii.	Salário Bruto até R$ 5.000,00 (inclusive) - desconto de 5%
iii.	Salário Bruto até R$ 7.500,00 (inclusive) - desconto de 10%
iv.	Salário Bruto acima de R$ 7.500,00 - desconto de 20% 
b.	Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
 Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00 - variado
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00 - fixo
        Total de descontos              : R$  165,00 - nao contou sindicato somente ir e inss
        Salário Liquido                 : R$  935,00 - bruto menos descontos
"""""

salBruto = 0.00
salLiquido = 0.00
totDes = 0.00
valHora = 0.00
qtdHora = 0
faixaIr = 0.00
desSind = 0.00
desIr = 0.00

valHora = float(input("Digite seu valor/hora:"))
qtdHora = int(input("Digite quantidade de horas trabalhadas:"))
salBruto = valHora * qtdHora
desSind = salBruto * 0.03

if salBruto <= 2000.00:
    faixaIr = 0
elif salBruto <= 5000.00:
    faixaIr = 0.05
elif salBruto <= 7500.00:
    faixaIr = 0.10
else:
    faixaIr = 0.20


desIr = salBruto * faixaIr
totDes = desIr + desSind
salLiquido = salBruto - totDes

print(f"Salário Bruto: ({qtdHora} * {valHora})       : R$ {salBruto}")
print(f"(-) IR ({int(faixaIr*100)}%)                      : R$  {desIr} ")
print(f"INSS ( 10%)                       : R$  {salBruto*0.10}")
print(f"(-) Sindicato ( 3%)               : R$  {salBruto*0.03}")
print(f"FGTS (11%)                        : R$  {salBruto*0.11}")
print(f"Total de descontos(sindicato+IR)  : R$  {totDes}")
print(f"Salário Liquido                   : R$  {salLiquido}")