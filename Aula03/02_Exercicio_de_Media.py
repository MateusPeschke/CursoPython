
quantidade_notas = int(input("Digite a quantidade de notas: "))

lista_notas = []
for i in range(quantidade_notas):
    nota = float(input(f"Digita a nota {i+1} : "))
    lista_notas.append(nota)

media = sum(lista_notas) / len(lista_notas)


if media < 5.5 :
    print("Reprovado")
elif media >= 7:
    print("Aprovado")
else:
    print("Recuperação")
print ( media)
print (lista_notas)