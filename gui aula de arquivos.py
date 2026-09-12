import os

print ("Aula de arquivos")

if os.path.isfile("login.txt"):
    print("Cadastro ja existe!")
    usuario = input("Digite seu usuario: ")
    senha = input("Digite sua senha: ")

    arquivo = open("login.db", "r")
    conteudo = arquivo.reasd()
    arquivo.close

    partes = conteudo.split("|", 2)

    if usuario == partes[0] and senha == partes[1]:
        print("Autenticado com sucesso! ")
        print("")
        print(f"Bem vindo {usuario}")
        print("")
    else:
        print("Usuario ou senha errados!")
else:
    print("Cadastro nao existe ainda, registre-se agora!")
    usuario = input("Digite seu usuario: ")
    senha = input("Digite sua senha: ")

    arquivo = open("login.db", "r")
    arquivo.write(f"{usuario}|{senha}")
    arquivo.close()

    print(f"Usuario {usuario} cadastrado com sucesso.")