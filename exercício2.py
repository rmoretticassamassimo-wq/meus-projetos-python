import os 
import time
try:
    consumo = float(input('Qual o consumo médio do veículo? '))
    distancia = float(input('Qual a distância a ser percorrida? '))

    quantidade = distancia / consumo

    print(quantidade)

except ValueError:
        print('Somente números, por favor.') #Combate o string
        time.sleep(1)
        os.system('cls')

except ZeroDivisionError:
        print('Divisão por zero') #Combate a divisão por zero
        time.sleep(1)
        os.system('cls')
        
except Exception:
        print('Erro: exceção') #Qualquer outro erro
        time.sleep(1.5)
        os.system('cls')