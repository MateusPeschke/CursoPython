
# Questão 1
lista = [x*3 for x in range(34)]

print(lista)

# Questão 2
lista_par = [x for x in range(100) if x%2 == 0]

print(lista_par)

# Questão 4

import matplotlib.pyplot as plt

def Jur_compostos(tempo,capital,taxa):
    taxa = taxa / 100
    montatante = capital * (1 + taxa) ** tempo 
    return round(montatante,2)    

tempo = [ x for x in range(48)]
# montatante = [round(100*(1+0.03)**t,2) for t in tempo ]

montatante = [ Jur_compostos(t,100,3) for t in tempo]
tem_mont = len(montatante)

if len(tempo) == tem_mont :
    plt.plot(tempo,montatante)
    plt.show()