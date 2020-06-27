# caixa eletronico 
# criar um caixa que mostre a quantidado de notas para completar a quantidade requerida!



valor_requerido = float(input('Digite o valor requerido :'))

while True:

    if valor_requerido >= 100:
        valor_requerido = valor_requerido - 100
    if valor_requerido >= 50:
        valor_requerido = valor_requerido - 50
    if valor_requerido >= 20:
        valor_requerido = valor_requerido - 20
    if valor_requerido >= 10:
        valor_requerido = valor_requerido - 10
    if valor_requerido >= 5:
        valor_requerido = valor_requerido - 5
    if valor_requerido >= 2:
        valor_requerido = valor_requerido - 2
    if valor_requerido >= 1:
        valor_requerido = valor_requerido - 1
    if valor_requerido >= 0.5:
        valor_requerido = valor_requerido - 0.5
    if valor_requerido >= 0.25:
        valor_requerido = valor_requerido - 0.25
    if valor_requerido >= 0.1:
        valor_requerido = valor_requerido - 0.1
    if valor_requerido >= 0.05:
        valor_requerido = valor_requerido - 0.05
    if valor_requerido >= 0.01:
        valor_requerido = valor_requerido - 0.01

print(valor_requerido)
