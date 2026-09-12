print("Calculadora basica")

def soma(numero1,numero2):
    return numero1 + numero2

def subtracao(numero1,numero2):
    return numero1 - numero2


selecao = -1
while selecao != "s":
    print("")
    print("Escolha uma funcao digitando '+' ou '-', 's' para sair")
    selecao = input("Digite uma opcao:")

    if selecao == "s":
        break

    numero1 = float(input("Digite o primeiro numero: "))
    numero2 = float(input("Digite o segundo numero: "))
    if selecao == "+":
        print( soma(numero1,numero2)   )
    elif selecao == "-":
        print(  subtracao(numero1, numero2)   )
    elif selecao == "*":
        print("")
    elif selecao == "/":
        print("")
    elif selecao == "**":
        print("")
    elif selecao == "***":
        print("")
        