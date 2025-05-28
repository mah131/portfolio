valor = float(input("Digite o valor do produto: R$ "))

desconto_percentual = float(input("Digite o percentual de desconto (%): "))

desconto_valor = (desconto_percentual / 100) * valor

valor_com_desconto = valor - desconto_valor

print(f"\nValor original: R$ {valor:.2f}")
print(f"Desconto de {desconto_percentual:.1f}%: R$ {desconto_valor:.2f}")
print(f"Valor com desconto: R$ {valor_com_desconto:.2f}")