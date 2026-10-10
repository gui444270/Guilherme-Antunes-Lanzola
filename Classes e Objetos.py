print("Classe e Objetos: Programacao Orientada a Objeto")

class aluno():
    nome = ""
    idade = ""
    nota = 0
    anotacoes = ""
    ativo = True

    def __init__(self, nome, idade, nota, anotacoes, ativo):
        self.nome = nome
        self.idade = idade
        self.nota = nota
        self.anotacoes = anotacoes
        self.ativo = ativo

    def ativar(self):
        self.ativo = True

    def destivar(self):
        self.ativo = False

    def aprovado(self):
        if self.nota >= 6:
            return "Aprovado"
        else:
            return "Reprovado"

aluno1 = aluno (nome = "Guilherme", idade = "15", anotacoes = "Aluno CTRL Play", nota = 7, ativo = True)

print(aluno1)

print("Desativando aluno")
aluno1.desativar()
                                                                                                                                                      
passou = aluno1.aprovado()
print(f"Situacao do aluno; {passou}")
