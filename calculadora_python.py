# Calculadora em Python.

# Menu com as opções.

import os

def menuOpcoes():
    os.system("cls")
    print ("Escolha uma opção:")
    print("1 - Soma.")
    print("2 - Subtração.")
    print("3 - Divisão.")
    print("4 - Multiplicação.")
    print("5 - Sair da Calculadora")

# Opção 01

def soma():  
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    resultado = num1 + num2
    print("O resultado da soma é igual a " + str(resultado) + ".")
    os.system("pause")
    
# Opção 02

def subtracao():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    resultado = num1 - num2
    print("O resultado da subtração é igual a " + str(resultado) + ".")
    os.system("pause")

# Opção 03

def divisao():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    resultado = num1 / num2
    print("O resultado da divisão é igual a " + str(resultado) + ".")
    os.system("pause")

# Opção 04

def multiplicacao():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    resultado = num1*num2
    print("O resultado da multiplicação é igual a " + str(resultado) + ".")
    os.system("pause")

# Opção 05 

def sair():
    print("A calculadora foi encerrada.")

opc = 0

while opc != 5:
    menuOpcoes()
    opc = int(input("Digite uma Opção: "))
    if opc == 1:
        soma()
    elif opc == 2:
        subtracao()
    elif opc == 3:
        divisao()
    elif opc == 4:
        multiplicacao()
    elif opc == 5:
        os.system("cls")
        sair()
    else:
        os.system("cls")
        print("Opção Inválida.")
        os.system("pause")

        
        