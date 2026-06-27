saldo = 1000
valor_saque = int(input("Informe um valor para saque: "))
while valor_saque > saldo:
    print("Saldo insuficiente")
    valor_saque = int(input("Informe um valor para saque: "))
print("saque realizado")
print(f"saldo restante: R$", {saldo - valor_saque})