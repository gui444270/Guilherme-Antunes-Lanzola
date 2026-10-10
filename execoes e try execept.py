print("Exeções e Try Execept")

try:
    pass
except:
    pass
finally:
    pass

opcao = 0

while opcao != 4:
    print("Super programa 9000")
    print("1. um")
    print("2. dois")
    print("3. tres")
    print("4. quatro")

    try:
        opcao = int(input("Digite sua escolha") )
    except:
        print("Digite um numero!")
    else:    
     if opcao == 1:
        print("Opção 1 selecionada")
     elif opcao == 2:
        print("Opção 2 selecionada")
     elif opcao == 3:
        print("Opção 3 selecionada")
     elif opcao == 4:
        print("Opção 4 selecionada")
     else:
        print("Opção invalida")
