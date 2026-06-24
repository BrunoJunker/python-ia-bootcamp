#Calcular quantos dias um produto duraria se a pessoa usar x proções por dia

produto = input('Digite o nome do produto: ')
total_de_porcoes = int(input('Digite quantas porções tem o produto: '))
porções_por_dia = int(input('Digite a quantidade de porções que você usa por dia: '))
dias = total_de_porcoes / porções_por_dia

#print(f'O produto {produto} duraria {int(dias)} dias se você usar {porções_por_dia} porções por dia')
print(f'O produto {produto} duraria {dias:.0f} dias se você usar {porções_por_dia} porções por dia')
