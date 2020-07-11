# zip()
# lambda()
# filter()
# reduce()
# map()

# Função lambda
# var = lambda <lista de variaveis> : <expressão>
# var = lambda <lista de variaveis> : <expressão> if <condição> else <expressão2>
# soma = lambda numero1, numero2: numero1 + numero2

def soma (val,val2):
    return val + val2

print(soma(10,15))
#######################################
print("\n")
soma_lb = lambda var1,var2: var1 + var2

print(soma_lb(10,15))
#######################################
multiplica_lb = lambda var1,var2: var1 * var2

print(multiplica_lb(10,15))
print("\n")

def cadastro (nome,idade = 18,sexo = "N/D"):
    print(f"seu nome é {nome}, você tem {idade} anos e é do sexo {sexo}" )
print("\n")
# Lista
Lista = ["Abioluz",23,"M"]
cadastro("luiza",19,"LGBT")
cadastro(*Lista)

# Errado
## Deve ter a mesma quantidade de items e estar na ordem correta
# Lista = ["Abioluz",23,"M","Mateus"]
# cadastro(*Lista)
## A ordem importa
# Lista = ["Abioluz","M",23]
# cadastro(*Lista)

print("\n")
# Dicionario
Dicionario = {"nome": "Abioluz", "sexo": "M","idade":23}
cadastro(**Dicionario)


# div_lb = lambda valor1,valor2: valor1/valor2 if 
print("\n")
Lista2 = [0,1,2,3,4]
espo= lambda x,y=0: x**2+y
Lista2_resultato = list(map(espo,Lista2))
print(Lista2_resultato)
print(espo(2,5))

print("\n")
lista3 = [0,1,2,3,4,5,6,7,8,9,10]
lista3_resultato= list(map(lambda m: m * 3,lista3))
print(lista3_resultato)

print("\n")
t = [i for i in range(24)]
Jur_simples = lambda t,valor=200, i=10: round(valor*(1+(i/100))*t,2)
mont = list(map(Jur_simples,t))
print(mont)
print(Jur_simples(8,500,16))
print("\n")


lista4 = ["m","f","m","f","m","f"]
Filtro = lambda sexo: True if sexo == "m" else False
resultado = list(filter(Filtro,lista4))
print(lista4)
print(resultado)




lista5 = [i for i in range(30)]
mult_tres = lambda multp: True if (multp%3)==0 else False
resultado_mult = list(filter(mult_tres,lista5))
resultado_mult_fil = list(filter(lambda multp: True if (multp%3)==0 else False, range(30)))
print(lista5)
print(resultado_mult)
print(resultado_mult_fil)


from random import randint as rd
funcao = lambda x: True if x == "f" else False
lista6= [ "f" if(rd(0,1)==1) else "m" for i in range(20)]
print(lista6)
print(list(filter(funcao,lista6)))

from random import randint
lista7 = [randint(0,10) for i in range(20)]
filtro2 = lambda x: True if lista7.count(x) == 1 else False
print(lista7)
print(list(filter(filtro2,lista7)))
print("\n")
from functools import reduce

lista8= [i for i in range(50)]
funcao2 = lambda x,y: x+y
print(lista8)
print(reduce(funcao2,lista8))
print("\n")

lista9= [1,1,2,3,3,4,4,5,6,6,15,15]
funcao2 = lambda x,y: x^y
print(lista9)
print(reduce(funcao2,lista9))