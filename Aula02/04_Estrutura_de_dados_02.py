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
aluno1 = {'nome':'Maycon','sobrenome':'Granemann','idade':18,'lista_notas':[10,8,9,7]}
aluno2 = {'nome':'Mateus','sobrenome':'Peschke','idade':22,'lista_notas':[7,6,8,9]}
lista = [aluno1,aluno2]
print(aluno1)
print(aluno1['nome'])
for a in lista:
    print(a['nome'])
    print(a['sobrenome'])
    print(a['idade'])
    print(a['lista_notas'])

# dict_numero={'n1':10,2:3,3:5}
# print(dict_numero)


