#"Exercicio 3-Faça um programa que pergunte:
#"o preço de três produtos e informe qual produto você deve comprar,
#"sabendo que a decisão é sempre pelo mais barato".


p1 = input("Digite o preço 1: ")
p2 = input("Digite o preço 2: ")
p3 = input("Digite o preço 3: ")


def menor():
    if p1 < p2 and p3 and p1:
        print('O produto 1 é o mais barato!')
    elif p2 < p1 and p3:
        print('O produto 2 é o mais barato!')
    elif p3 < p1 and p2:
        print('O produto 3 é o mais barato!')

    elif p1 == p2 and p1 and p2 < p3:
        print('O produto 1 e 2 são os mais baratos!')
    elif p1 == p3 and p1 and p3 < p2:
        print('O produto 1 e 3 são os mais baratos!')
    elif p2 == p3 and p2 and p3 < p1:
        print('O produto 1 e 2 são os mais baratos!')

    else:
        print('Todos os preços são iguais!')

menor()
