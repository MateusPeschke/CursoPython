# caixa eletronico 
# criar um caixa que mostre a quantidado de notas para completar a quantidade requerida!



valor_requerido = float(input('Digite o valor requerido :'))
quant001 = 0
quant100 = 0
quant50 = 0
quant20 = 0


while True:

    if valor_requerido >= 100:
        valor_requerido = valor_requerido - 100
        quant100 = quant100 + 1
    if valor_requerido >= 50:
        valor_requerido = valor_requerido - 50
        quant50 = quant50 + 1
    if valor_requerido >= 20:
        valor_requerido = valor_requerido - 20
        quant20 = quant20 + 1
    if valor_requerido >= 10:
        valor_requerido = valor_requerido - 10
        quant10 = quant10 + 1
    if valor_requerido >= 5:
        valor_requerido = valor_requerido - 5
        quant5 = quant5 + 1
    if valor_requerido >= 2:
        valor_requerido = valor_requerido - 2
        quant2 = quant2 + 1
    if valor_requerido >= 1:
        valor_requerido = valor_requerido - 1
        quant1 = quant1 + 1
    if valor_requerido >= 0.5:
        valor_requerido = valor_requerido - 0.5
        quant105 = quant05 + 1
    if valor_requerido >= 0.25:
        valor_requerido = valor_requerido - 0.25
        quant025 = quant025 + 1
    if valor_requerido >= 0.1:
        valor_requerido = valor_requerido - 0.1
        quant01 = quant01 + 1
    if valor_requerido >= 0.05:
        valor_requerido = valor_requerido - 0.05
        quant005 = quant005 + 1
    if valor_requerido >= 0.01:
        valor_requerido = valor_requerido - 0.01
        quant001 = quant001 + 1

    print()
