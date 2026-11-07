# 2. Receba ano de nascimento e ano atual. Calcule idade e semanas.

# Entrada
AnoNascimento = int(input("Digite o ano: "))
AnoAtual = int(input("Digite o ano" ))
# Processamento
idade = AnoAtual - AnoNascimento
idadadeSemanas = 4 * 12 * idade

# Saída
print(f"Sua idade é: {idade} ano(s)")
print(f"Sua idade em semanas: {idadadeSemanas} semana(s)")