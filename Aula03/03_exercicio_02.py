# num = int(input("Digite um numero entra 10 a 100: "))

# cont = 10
# while cont <= num:
#     cont = cont + 1
#     if (cont % 2) == 0:
#         continue
#     else:
#         print(cont)


menu = input('''
Menu:

1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão
S - Sair

Digite a opção desejada: 
''')
num1 = int(input('Digite o numero: '))
num2 = int(input('Digite o numero: '))

while menu != 'S':
    if menu == '1':
        soma = num1 + num2
        print(soma)
    elif menu == '2':
        sub = num1 - num2
        print(sub)
    elif menu == '3':
        mult = num1 * num2
        print(mult)
    else:
        div = num1 / num2
        print(div)
    continue
