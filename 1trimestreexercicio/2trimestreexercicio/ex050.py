soma = 0
cont = 0

# Percorre o intervalo de 1 até 500
for c in range(1, 501):
    # Verifica se o número é ímpar e múltiplo de 3
    if c % 2 != 0 and c % 3 == 0:
        soma += c
        cont += 1

print(f'A soma de todos os {cont} valores solicitados é {soma}.')