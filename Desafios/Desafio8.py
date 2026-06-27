saldo = 1000
ops = int(input("""
Selecione uma opção:
1 - Consultar saldo
2 - Sacar
3 - Depositar
4 - Sair
"""))
while ops != 4:
    if ops == 1:
        print("Seu saldo é de: R$", saldo)
    elif ops == 2: 
        valor_saque = int(input("Informe um valor para saque: "))
        if valor_saque > saldo:
            print("Saldo insuficiente")
        else:
            print("saque realizado")
            
            print("saldo restante: R$", saldo - valor_saque)
            
    elif ops == 3:
        deposito = int(input("Digite o valor para deposito: "))
        saldo = saldo + deposito
        print("Deposito realizado com sucesso")
        print("Saldo total: R$",saldo)
    ops = int(input("""
Selecione uma opção:
1 - Consultar saldo
2 - Sacar
3 - Depositar
4 - Sair
    """))

print("Sistema encerrado")