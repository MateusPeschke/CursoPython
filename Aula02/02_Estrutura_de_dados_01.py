# list - Lista - '[...]'
# dict - Dicionario
# tuple - Tuplas


idades = 181
lista_idades = [18,19,50,19,20,56,98,85,79]



print(idades)

# imprimindo lista toda
print(lista_idades)

# imprimir um item especifico da lista
print(lista_idades [1])

# Remove um item da lista
lista_idades.remove(19)
print(lista_idades)

# Removando dado com a função "POP" -
# Função remove pela posição do dado e retorna o valor do dado
retorno_do_pop = lista_idades.pop(1)
print(lista_idades)
print(retorno_do_pop)

# Removendo todos os itens da lista
# lista_idades.clear()
# print(lista_idades)


# Adicionando dados na lista
lista_idades.append(idades)
print(lista_idades)
lista_idades.append(19)
print(lista_idades)

# Mostrando a quantidade de um determinado dado da lista
print(lista_idades.count(19))

# Mostrando o número total de dados da lista
# "len" utilisado para contar quantas unidades tem em uma determinada lista
print( len(lista_idades))

# Fatiamento de lista
# imprimindo os 3 primeiros itens
print(lista_idades[:3])

# imprimindo os 3 ultimos numeros
index_antepenultimo_item = len(lista_idades)-3
print(lista_idades[index_antepenultimo_item : ])

# Imprimindo meio da lista
print(lista_idades[2:6])

print(lista_idades)
lista_idades.reverse()
print(lista_idades)

# Inserindo um dado em uma posição específica da lista
lista_idades.insert(2,152)
print(lista_idades)


# Inserindo o numero 153 após o 152
index = lista_idades.index(152)
lista_idades.insert(index+1,153)
print(lista_idades)

# Alterar dado em uma posição específica
lista_idades[0] = 150
lista_idades[1] = 151
lista_idades[4] = 154
print(lista_idades)