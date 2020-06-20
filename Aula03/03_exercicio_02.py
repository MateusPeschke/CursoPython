# num = int(input("Digite um numero entra 10 a 100: "))

# cont = 10
# while cont <= num:
#     cont = cont + 1
#     if (cont % 2) == 0:
#         continue
#     else:
#         print(cont)



def teclado():
    num1_fun = int(input('Digite o numero: '))
    num2_fun = int(input('Digite o numero: '))
    return num1_fun,num2_fun

def menu_fun():
    menu = '''
Menu:

1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão
S - Sair

Digite a opção desejada: 
'''
    print(menu)

def soma (num1_fun,num2_fun):
    soma = num1_fun + num2_fun
    return soma

def sub (num1_fun,num2_fun):
    sub = num1_fun - num2_fun
    return sub

def mult (num1_fun,num2_fun):
    mult = num1_fun * num2_fun
    return mult

def div (num1_fun,num2_fun):
    div = num1_fun / num2_fun
    return div

while True:

    menu_fun()

    opcao = input()
    
    if opcao == '1':
        num1,num2 = teclado()
        soma_res = soma(num1,num2)
        print(f'O resultado é : {soma_res}')

    if opcao == '2':
        num1,num2 = teclado()
        sub_res = sub (num1,num2)
        print(f'O resultado é : {sub_res}')

    if opcao == '3':
        num1,num2 = teclado()
        mult_res = mult(num1,num2)
        print(f'O resultado é : {mult_res}')

    if opcao == '4':
        num1,num2 = teclado()
        div_res = div(num1,num2)
        print(f'O resultado é : {div_res}')

    if opcao.upper() == 'S':
        print("Saindo...")
        break
    

