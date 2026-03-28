import os
import time

print('========== Exercício 1 ==========')
while True:
    try:
        velocidade = float(input('Qual a velocidade média em km/h: '))
        tempo = float(input('Qual o tempo de viagem em horas?: '))

        distancia = velocidade * tempo

        print(f'A distância percorrida pelo veículo é: {distancia:.2f}')
        break

    except ValueError:
        print('Somente números, por favor.') #Combate o string
        time.sleep(1)
        os.system('cls')

    except Exception:
        print('Erro: exceção') #Qualquer outro erro
        time.sleep(1.5)
        os.system('cls')

resposta = input('Deseja fazer outro cálculo?\n s pra SIM e n para NÃO')

if resposta.lower() == 'n':
    print('Encerrando programa...')
time.sleep(1.5)
os.system('cls') 