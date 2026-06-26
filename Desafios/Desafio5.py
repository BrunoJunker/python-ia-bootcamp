senha = int(input("Digite a senha: "))
tentativas = 0
while senha != 1234 and tentativas < 3:
    print('senha incorreta, tente novamente')
    tentativas += 1
    senha = int(input("Digite sua senha: "))
if senha == 1234:
   print('Acesso permitido')
else:
    print("sistema bloqueado")
    