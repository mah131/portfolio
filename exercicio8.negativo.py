print("__________Contador de Números Negativos__________")

numeros = []  # vetor (lista) para armazenar os 4 números

# Coletar 4 números do usuário
for i in range(4):
    num = float(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

# Contar quantos são negativos
negativos = 0
for n in numeros:
    if n < 0:
        negativos += 1

# Mostrar resultado
print(f"\nVocê digitou {negativos} número(s) negativo(s).")