
lista_alunos = []

for i in range(2):
    dict_alunos = {}
    dict_alunos['nome'] = input('digite seu nome: ')
    dict_alunos['sobrenome'] = input('digite seu sobrenome: ')
    dict_alunos['idade'] = input('digite sua idade: ')
    lista_alunos.append(dict_alunos)

print('\n')
for a in lista_alunos:
    print("Usuario Cadastrado:",a['nome'],a['sobrenome'],a['idade'])