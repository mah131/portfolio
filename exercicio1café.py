print("Bem-vindo a nossa cafeteria!")
#Pergunte o valor do café
valor_cafe = float(input("Qual é o valor de um café? R$"))

#Pergunta quantos cafés o usuário quer comprar
quantidade = int(input("Quantos cafés você quer comprar?"))

#Calcula o total a pagar
total = valor_cafe * quantidade

#Exibir o resultado
print(f"Você deve pagar R$ {total:.2f}")