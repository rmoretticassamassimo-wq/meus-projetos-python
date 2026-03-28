import os
import time
try:
    num1 = float(input('Digite um número: '))
    num2 = float(input('Digite outro número: '))
    operador = input ('digite (+), (-), (*), (/) ')
    resultado = 0

    match(operador):
        case "+":
            resultado = num1 + num2
        case "-":
            resultado = num1 - num2
        case "*":
            resultado = num1 * num2
        case "/":
            resultado = num1 / num2 
        case _:
            resultado = None

    if resultado != None:
        print(f"{num1} {operador} {num2} = {resultado}")
    else:
        print('operador inválido')

except ValueError:
        print('Somente números, por favor.') #Combate o string
        time.sleep(1)
        os.system('cls')
