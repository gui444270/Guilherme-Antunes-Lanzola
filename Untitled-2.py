import os

print("Aula de revisao, funcoes, input output, arquivos, loops")

def bemvindo(nome):
    print(f"Seja bem vindo{nome}")

nome = input()
bemvindo(nome)

arquivo = open("arquivo.txt", "w")
arquivo.write("O thiago e velho")
arquivo.close()

alunos = ["Davi l", "Davi", "Gui"]
for nome in alunos :
    print(f"Aluno: {nome}")

for numero in range(1000):
    print(numero)