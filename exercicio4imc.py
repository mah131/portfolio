print("Cálculo de IMC")
#Solicita os dados do usuário
idade = int(input("Digite sua idade em anos:"))
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
#Calcula o IMC
IMC = peso / (altura * 2)
#exibe o resultado.
print(f"\nIdade: {idade} anos")
print(f"Peso: {peso} kg")
print(f"Altura: {altura} m")
print(f"Seu IMC é: {IMC:.2f}")
