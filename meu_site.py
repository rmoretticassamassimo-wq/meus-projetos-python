import requests

resposta = requests.get("https://youtube.com")

print(f"O status do site é: ", resposta.text)