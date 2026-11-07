# 4. Receba nome, peso e altura. Calcule IMC.

nome = input("Digite seu nome: ")
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

imc = peso / (altura * altura)

print(f"imc: {imc:.2f}")