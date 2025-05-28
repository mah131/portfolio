principal = float(input("Digite o valor principal (R$):"))
taxa_juros = float(input("Digite a taxa de juros anual (%):"))
anos = int(input("Digite o número de anos: "))

montante = principal + (principal * taxa_juros * anos / 100)

print(f"O montane final após {anos} anos será R$ {montante:.2f}")