valor_compra = float(input("Digite o valor da compra: "))
estado = input("Digite o seu estado (SP, RJ, PR, SC, RS): ").upper()
frete = 0
if estado not in ["SP", "RJ", "PR", "SC", "RS"]:
    print("Estado não atendido. Por favor, digite um estado válido.")
else:
    if valor_compra > 300:
        print(" Frete gratis garantido na sua compra!")
    else:
        if estado == "SP":
            frete = 10
        elif estado == "RJ":
            frete = 30
        elif estado == "PR":
            frete = 20
        elif estado == "SC":
            frete = 15
        elif estado == "RS":
            frete = 25
    print(f"Valor da sua compra: R$ {valor_compra}")
    print(f"Valor Frete: R$ {frete}")
    print(f"O valor total é R$ {valor_compra + frete}")