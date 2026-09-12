print("Calculadora de IMC")

peso = float( input("Qual seu peso em quilos") )
altura = float( input("Qual sua altura em metros") )
imc = peso / (altura**2)
if imc < 18.5:
    print(f"classificado como 'Abaixo do peso'")
if imc >= 18.5 and imc < 24.9:
    print(f"classificado como 'Peso normal'")
if imc >= 25 and imc < 29.9:
    print(f"classificado como 'Sobrepeso'")
if imc >= 30 and imc < 34.9:
    print(f"classificado como 'Obesidade Grau I'")
if imc >= 35 and imc < 39.9:
    print(f"classificado como 'Obesidade Grau II'")
if imc >= 40:
    print(f"classificado como 'Obesidade Grau III'")