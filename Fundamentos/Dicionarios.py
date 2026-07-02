# usuario = {
#     'nome': 'Bruno',
#     'idade': 26,
#     'Departamento':'TI'
# }

# usuario['idade'] = 20
# usuario['Cidade'] = 'Joinville'

# print(usuario)

aluno = {
    'nome': input('Nome do Aluno: '),
    'idade': input('idade do Aluno: '),
    'nota': input('Nota do Aluno: ')
}
print(f"{aluno['nome']} tem {aluno['idade']} anos de idade e tirou uma nota  {aluno['nota']}.")