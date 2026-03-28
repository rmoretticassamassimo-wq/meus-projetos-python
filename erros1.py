#tratamento de erros
import os
import time
while True:
    try:
        dividendo = int(input('Digite o dividendo:\n'))
        divisor = int(input('Digite o divisor:\n'))

        resultado = dividendo/divisor

        print(f'{resultado:.2f}')
        break
    
    except ValueError:
        print('Somente números, por favor.') #Combate o string
        time.sleep(1)
        os.system('cls')
        
    except ZeroDivisionError:
        print('Divisão por zero') #Combate a divisão por zero
        time.sleep(1)
        os.system('cls')
