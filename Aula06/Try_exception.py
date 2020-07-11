b= 10
c= 4
try :
    a = b/c
    
except ZeroDivisionError:
    a = "Não pode ser dividido por zero"
print(a)


try:
    arquivo = open("nome","r")
except FileNotFoundError:
    print("Arquivo não encontrado")
finally:
    arquivo.close()



with open("nome","r") as arquivo:
    pass


from contextlib import closing
with closing(open("nome","r")) as arquivo:
    pass

