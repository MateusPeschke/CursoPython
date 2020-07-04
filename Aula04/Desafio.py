# caixa eletronico 
# criar um caixa que mostre a quantidado de notas para completar a quantidade requerida!


dinheiro = [100,50,20,10,5,1,0.5,0.1,0.05,0.01]
valor = float(input("Digite o valordesejado: "))
for pila in dinheiro:
    quantidade = int(valor // pila)
    valor = round(valor % pila,2)
    # valor = valor - (pila * quantidade)

    print(f"{quantidade:d} nota(s) valor {pila:>6.2f} "
        if pila > 1 else
            f"{quantidade:d} moeda(s) valor {pila:>6.2f}")

