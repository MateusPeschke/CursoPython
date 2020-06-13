# tuplas
# O conjunto de dados não podem ser alterados
tupla = (10,12,13,15,18,20)
print(tupla)
print(tupla[1])
print(tupla[1:3])


# Código abaixo gera exceção pois a tupla não permite alteração
# tupla[1] = 88

# Crinando tuplas com tipos de dados diferentes, incluindo listas
tupla_aluno = ('Maykon','Diego',15,[10,8,5,6])

# Modificando o item da lista dentro da tupla
tupla_aluno[3][2] = 8
print(tupla_aluno)

# convetendo tupla em lista
lista_aluno = list(tupla_aluno)
print(lista_aluno)


# Dicionario
dict_alunos = {'nome':'Maycon','sobrenome':'Granemann','idade':18}
dict_alunos = {'nome':'Mateus','sobrenome':'Peschke','idade':18}
print(dict_alunos)
print(dict_alunos['nome'])

# dict_numero={'n1':10,2:3,3:5}
# print(dict_numero)


