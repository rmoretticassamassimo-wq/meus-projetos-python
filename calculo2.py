import os
import time
try:
    def soma(num1, num2):
        return num1 + num2

    def subtracao(num1, num2):
        return num1 - num2

    def multiplicacao(num1, num2):
        return num1 * num2

    def divisao(num1, num2):
        return num1 / num2

    def calc(operador, num1, num2):
        match operador:
            case "+":
                return soma(num1, num2)
            case "-":
                return subtracao(num1, num2)
            case "*":
                return multiplicacao(num1, num2)
            case "/":
                return divisao(num1, num2)
            case _:
                return None
        
    operador = input('Digite o operador (+), (-), (*), (/): ')
    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite outro número: "))
    resultado = calc(operador, num1, num2)
    print(f"O resultado é {resultado:.2f}")
except ValueError:
        print('Somente números, por favor.') #Combate o string
        time.sleep(1)
        os.system('cls')