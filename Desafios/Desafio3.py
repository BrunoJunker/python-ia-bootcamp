Idade = int(input('digite sua idade: '))
if Idade <= 17:
    print('Reprovado')
else:
    experiencia = input('Você tem experiencia na area? (s/n): ')
    if experiencia == 's':
        print('Aprovado para entrevista')
    else:
        print('Banco de Talentos!')
