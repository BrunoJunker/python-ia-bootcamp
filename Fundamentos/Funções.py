# def saudacao(nome, idade):
#     print(f'Olá {nome}, voce tem {idade} anos!')
# saudacao('andre', 25)
# saudacao('maria', 30)

# def somar(num1, num2):
#     return num1 + num2 #armazena o resultado da soma e retorna para quem chamou a função

# total = somar(10, 20) #chama a função e armazena o resultado na variavel total
# print(f' o resutlado da soma é de: {total}')


def calcular_desconto(preco, porcentagem):
    valor_final = preco - (preco*(porcentagem/100))
    return valor_final

valor_final = calcular_desconto(100, 10)
print(f'O valor final com desconto é de R${valor_final:.2f}')