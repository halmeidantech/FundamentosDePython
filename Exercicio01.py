# 1. Receba a idade em anos e imprima em meses, dias, horas e minutos.

# Entrada
idade = int(input("Digite a idade: ")) #pega o texto e converte para número inteiro(INT)

# processamento
idadeEmMeses = idade * 12
idadeEmDias = idade * 365
idadeEmHoras = idadeEmDias * 24
idadeEmHoras = idadeEmHoras * 60

# Saida
print (f"Sua idade em meses é: {idadeEmMeses} meses")
print (f"Sua idade em dias é: {idadeEmDias} dias")
print (f"Sua idade em horas é: {idadeEmHoras} horas")
print (f"Sua idade em minutos é: {idadeEmHoras} minutos")