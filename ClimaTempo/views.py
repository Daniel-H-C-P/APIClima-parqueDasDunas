from django.http import HttpResponse
from django.shortcuts import render
import json

def ClimaParque(request):
	#Para abrir o arquivo climaAgora
	with open('ClimaTempo/climaAgora.json') as f:
		data = json.load(f)
 
	#Lendo o arquivo
	clima = data['weather'][0]['description']

	#Para abrir o arquivo clima5dias
	with open('ClimaTempo/clima5dias.json') as g:
  		data2 = json.load(g)
 
	#Lendo e organizando o arquivo
	previsao = ""
	numheader = 0
	while numheader < 40:
		climaprint = str(data2['list'][numheader]['dt_txt']) + " " + str(data2['list'][numheader]['weather'][0]['description'])  + '\n '
		previsao += climaprint
		numheader +=1

	return HttpResponse("O clima agora no parque das duas é: " + str(clima) +'\n\n\n' + 'Previsão para os próximos dias:\n' + str(previsao))
	#Tirar a minha chave daqui e colocar em um arquivo com .gitignore


#def ClimaParqueRender(request):
#	return render(request, 'index.html')

