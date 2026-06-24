# numero = int(input('Digite um numero:'))
# if numero == 10:
#     print('Acertou o numero')
# else:
#     print('Errou o numero')

#---------------------------------

# Idade = int(input('Digite sua idade:'))
# if Idade <=17:
#     print('Você é menor de idade')
# else:
#     print('Voce é maior de idade')

#---------------------------------

# nota = float(input('Digite sua nota: '))
# if nota >=7:
#     print('Aprovado')
# elif nota >=5:
#     print('Recuperação')
# else:
#     print('Reprovado')

#---------------------------------

# usuario = input('Digite seu usuario: ')
# senha = input('Digite sua senha: ')

# if usuario == 'admin' and senha == '123admin':
#     print('Acesso permitido')
# else:
#     print('Acesso negado') 

#---------------------------------

Idade = int(input('digite sua idade: '))
if Idade >= 18:
    print('Você tem acesso ao site')
elif Idade >= 16:
        Autorização = input('Você tem autorização dos pais? (S/N): ')
        if Autorização == 'S':
            print('Você tem acesso ao site com autorização dos pais')
        else:
            print('Você não tem acesso ao site')
