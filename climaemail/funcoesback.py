import requests
import time

climaAgora = requests.get('https://api.openweathermap.org/data/2.5/weather?id=3394023&lang=pt&APPID=9e70fbffdde1b3cfcb57ddd5f3a250b4').json()
clima5dias = requests.get('https://api.openweathermap.org/data/2.5/forecast?id=3394023&lang=pt&APPID=9e70fbffdde1b3cfcb57ddd5f3a250b4').json()
executar = 1
num = 1	

def pegaClima():
	#executando a primeira querry:
	climaAgora
	#criando o primeiro arquivo json:
	with open('climaAgora.json', 'w') as fh1:
		fh1.write(str(climaAgora).replace("'", '"', 1000))
	#executando a segunda querry:
	clima5dias
	#criando o segundo arquivo json:
	with open('clima5dias.json', 'w') as fh2:
		fh2.write(str(clima5dias).replace("'", '"', 10000))
#loop do arquivo:
pegaClima()
print('pesquisa completa!')