print("Validador de e-mail")
email = input("Digite seu email: ")

if email.find("@gmail.com") == -1:
    print("Email Invalido")
else:
    print("Email Valido")
    print(f"Tamanho do Email: {len(email)}")
    print(f"Primeira letra do email: {email[0]}")

    print(f"Existem {email.count("a")} letras a neste email")

    print(f"Email maisculo {email.upper()}")
    print(f"Email minusculo {email.lower()}")

    partes = email.split("@")
    
    print(f"Email antes do arroba: {partes[0]}")
    print(f"Email depois do arroba: {partes[1]}")
    