# for repetir in range(5):
#     print(repetir)

#------------------------------

# for A in range(1,6):
#     print(A * 0.5)

#------------------------------

# for A in range(10, 0, -2):
#     print(A )

#------------------------------

# A = 0
# while A < 5:
#     print(A)
#     A = A + 1
#     # A += 1

senha = int(input('Digite sua senha: '))
while senha != 1234:
    print('senha incorreta, tente novamente')
    senha = int(input('Digite sua senha: '))
print('Acesso permitido')
