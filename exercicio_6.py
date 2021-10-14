"""""
Faça um Programa que leia um número e exiba o dia correspondente da semana. (1 - Domingo, 2 - Segunda, etc.), 
se digitar outro valor deve aparecer valor inválidos.
"""""

diaSemana = ["0", "Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]

diaEscolhido = int(input("Digite o número do dia da semana de 1-7: "))

if diaEscolhido > 0 and diaEscolhido < 8:
    print(diaSemana[diaEscolhido])
else:
    print("Escolha um numero entre 1 e 7")
