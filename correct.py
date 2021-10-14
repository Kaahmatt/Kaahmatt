"""
Ler lista de nomes de arquivo e realizar sorteio destes nomes para 3 colocações,
sendo que a mesma pessoa não pode ser sorteada mais de uma vez.
Após finalização do sorteio, imprimir o resultado em tela, com
os nomes dos 1º, 2º e 3º ganhadores,
assim como escrever um arquivo com este resultado.
"""
import random

listaPessoas = []

print("iniciando a leitura dos nomes no arquivo...")
with open("C:\\arquivospy\\LISTA.txt", "r", encoding="latin1") as file:
    for linha in file:
        listaPessoas.append(linha)

print(f"{len(listaPessoas)} nomes lidos.")

resultadoSorteio = ""

#Realização do primeiro sorteio
numeroSorteado = random.randint(0, 9999)
resultadoSorteio = f"O vencedor do 1º sorteio é: {listaPessoas[numeroSorteado]}\n"
listaPessoas.pop(numeroSorteado)

#Realização do segundo sorteio
numeroSorteado = random.randint(0, 9998)
resultadoSorteio = resultadoSorteio + f"O vencedor do 2º sorteio é: {listaPessoas[numeroSorteado]}\n"
listaPessoas.pop(numeroSorteado)

#Realização do terceiro sorteio
numeroSorteado = random.randint(0, 9997)
resultadoSorteio = resultadoSorteio + f"O vencedor do 3º sorteio é: {listaPessoas[numeroSorteado]}\n"

print(resultadoSorteio)

with open("C:\\arquivospy\\ResultadoSorteio.txt", "w+") as file:
    file.write(resultadoSorteio)