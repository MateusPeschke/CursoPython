# "r" read - abre o arquivo
# "w" write - cria ou substitui um arquivo 
# "a" append - adiciona novas informações

import matplotlib.pyplot as plt
import numpy as np


arquivo = open(r"C:\Users\67184\Documents\Desenvolvimento_Agil_em_Python_1_2020\aula4\exemplos\cadastro.txt","r")
lista_cadastro = []
for pessoa in arquivo:
    pessoa = pessoa.strip()
    pessoa = pessoa.split(';')
    lista_cadastro.append(pessoa)
    
arquivo.close()

# for pessoa in lista_cadastro:
#     if pessoa[0].upper() == '300':
#         print(pessoa)
#         break

# for pessoa in lista_cadastro:
#     if pessoa[3].upper() == 'F':
#         print(pessoa)
#         # break

# for pessoa in lista_cadastro:
#     if not ('0' in pessoa[0]) and not ('A' in pessoa[1]):
#         print(pessoa)
#         # break

mulher = []
contador_mulher = 0 
for pessoa in lista_cadastro:
    if pessoa[3] == 'f':
        mulher.append(pessoa)
        contador_mulher = contador_mulher + 1
        # break

arquivo = open(r'C:\Users\67184\Documents\Desenvolvimento_Agil_em_Python_1_2020\aula4\exemplos\mulher.txt','w')
for pessoa in mulher:
    pessoa_str = ';'.join(pessoa)+"\n"
    arquivo.write(pessoa_str)

arquivo.close()

homens = []
contador_homens = 0
for pessoa in lista_cadastro:
    if pessoa[3] == 'm':
        homens.append(pessoa)
        contador_homens = contador_homens + 1
        # break
arquivo = open(r'C:\Users\67184\Documents\Desenvolvimento_Agil_em_Python_1_2020\aula4\exemplos\homens.txt','w')
for pessoa in homens:
    pessoa_str = ';'.join(pessoa)+"\n"
    arquivo.write(pessoa_str)

arquivo.close()

maior_idade = []
contador_maior = 0
for pessoa in lista_cadastro:
    if int(pessoa[2]) >= 18:
        maior_idade.append(pessoa)
        contador_maior = contador_maior + 1
        # break
arquivo = open(r'C:\Users\67184\Documents\Desenvolvimento_Agil_em_Python_1_2020\aula4\exemplos\maior_idade.txt','w')
for pessoa in maior_idade:
    pessoa_str = ';'.join(pessoa)+"\n"
    arquivo.write(pessoa_str)

arquivo.close()


menor_idade = []
contador_menor = 0
for pessoa in lista_cadastro:
    if int(pessoa[2]) < 18:
        menor_idade.append(pessoa)
        contador_menor = contador_menor + 1
        # break
arquivo = open(r'C:\Users\67184\Documents\Desenvolvimento_Agil_em_Python_1_2020\aula4\exemplos\menor_idade.txt','w')
for pessoa in menor_idade:
    pessoa_str = ';'.join(pessoa)+"\n"
    arquivo.write(pessoa_str)

arquivo.close()


x = np.linspace(0,2 * np.pi,400)
y = np.sin(x ** 2)
genero = ("Homens", "Mulheres")
quantidade_genero = (contador_homens,contador_mulher)

Idade = ('maior','menor')
quantidade_idade = (contador_maior,contador_menor)

plt.subplot(2,1,1)
plt.bar(genero,quantidade_genero)

plt.subplot(2,1,2)
plt.bar(Idade,quantidade_idade)


plt.show()