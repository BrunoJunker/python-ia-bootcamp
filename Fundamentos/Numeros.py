num1 = 10
num2 = 2

print(num1 + num2) #Soma
print(num1 - num2) #Subtração
print(num1 * num2) #Multiplicação
print(num1 / num2) #Divisão
print(num1 // num2) #Divisao inteira
print(num1 % num2) #Resto da divisão
print(num1 ** num2) #Exponenciação


preço = int(input('Digite o preço do produto: '))
desconto = int(input('Digite a % de desconto: '))

print(f'O preço do produto com desconto é: {preço - (preço * desconto / 100)}') 

