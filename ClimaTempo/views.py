from django.http import HttpResponse
from django.shortcuts import render
import json
import re
#from .leitor import *

"""
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

	#return HttpResponse("O clima agora no parque das duas é: " + str(clima) +'\n\n\n' + 'Previsão para os próximos dias:\n' + str(previsao))
	return render(request, 'index.html')
	#Tirar a minha chave daqui e colocar em um arquivo com .gitignore
"""


def ClimaParque2(request):
	########### variáveis chave: 'climaatual', 'dia1', 'dia2', 'dia3', 'dia4', 'dia5'.


	with open('ClimaTempo/climaAgora.json') as f:
		data = json.load(f)
	#Lendo o arquivo
	climaatual = data['weather'][0]['description']

	with open('ClimaTempo/clima5dias.json') as g:
		data2 = json.load(g)
	#Lendo o arquivo e criando uma lista
	numheader = 0
	previsao = []
	while numheader < 40:
		climaprint = (str(data2['list'][numheader]['dt_txt']).split( ))
		climaprint.append(str(data2['list'][numheader]['weather'][0]['description']))
		previsao.append(climaprint) 
		numheader +=1
	
	#Criando uma lista de dias
	dias = []
	separador = 0
	while separador < 40:
		daynum = str(previsao[int(separador)][0])
		dias.append(daynum)
		separador +=1
	diasuniq= list(set(dias))
	diasuniq.sort()
	#print(diasuniq)
	#print(len(diasuniq))

	# organizando tudo
	prevorganizada = []
	for x in diasuniq:
		prevorganizada.append([])
	y = 0
	for item in previsao:
		z = 0
		while z < len(diasuniq):
			if item[0] == diasuniq[z]:
				prevorganizada[z].append(item)
				z +=1
			else:
				z +=1
				continue
		y +=1		

	#exemplo de exibição das informações:
	#print("\nPrevisão para os próximos dias")
	"""
	dia1 = 'Dia {}'.format(prevorganizada[0][0][0])
	for num1 in prevorganizada[0]:
		dia1 += '\n' + (num1[1] + ": " + num1[2])

	dia2 = 'Dia {}'.format(prevorganizada[1][0][0])
	for num2 in prevorganizada[1]:
		dia2 += '\n' + (num2[1] + ": " + num2[2])
	
	dia3 = 'Dia {}'.format(prevorganizada[2][0][0])
	for num3 in prevorganizada[2]:
		dia3 += '\n' + (num3[1] + ": " + num3[2])

	dia4 = 'Dia {}'.format(prevorganizada[3][0][0])
	for num4 in prevorganizada[3]:
		dia4 += '\n' + (num4[1] + ": " + num4[2])

	dia5 = 'Dia {}'.format(prevorganizada[4][0][0])
	for num5 in prevorganizada[4]:
		dia5 += '\n' + (num5[1] + ": " + num5[2])
	"""
	prevfinal = ''
	numx = 0
	for num1 in prevorganizada:
		prevfinal+= ('\n\nDia {}:'.format(prevorganizada[numx][0][0]))
		for num2 in num1:
			prevfinal+= '\n' + (num2[1] + ": " + num2[2])
		numx +=1
		print(prevfinal)

	return render(request, 'index.html', {'clima': climaatual}, {'prev': prevfinal} )

#def ClimaParqueRender(request):
#	return render(request, 'index.html')

def ClimaParque3(request):
	########### variáveis chave: 'climaatual', 'dia1', 'dia2', 'dia3', 'dia4', 'dia5'.


	with open('ClimaTempo/climaAgora.json') as f:
		data = json.load(f)
	#Lendo o arquivo
	climaatual = data['weather'][0]['description']

	with open('ClimaTempo/clima5dias.json') as g:
		data2 = json.load(g)
	#Lendo o arquivo e criando uma lista
	numheader = 0
	previsao = []
	while numheader < 40:
		climaprint = (str(data2['list'][numheader]['dt_txt']).split( ))
		climaprint.append(str(data2['list'][numheader]['weather'][0]['description']))
		previsao.append(climaprint) 
		numheader +=1
	
	#Criando uma lista de dias
	dias = []
	separador = 0
	while separador < 40:
		daynum = str(previsao[int(separador)][0])
		dias.append(daynum)
		separador +=1
	diasuniq= list(set(dias))
	diasuniq.sort()
	#print(diasuniq)
	#print(len(diasuniq))

	# organizando tudo
	prevorganizada = []
	for x in diasuniq:
		prevorganizada.append([])
	y = 0
	for item in previsao:
		z = 0
		while z < len(diasuniq):
			if item[0] == diasuniq[z]:
				prevorganizada[z].append(item)
				z +=1
			else:
				z +=1
				continue
		y +=1		

	prevfinal = []
	prevorg2 = ''
	numx = 0
	for num1 in prevorganizada:
		prevorg2+= ('\n\nDia {}:'.format(prevorganizada[numx][0][0]))
		for num2 in num1:
			prevorg2+= '\n' + (num2[1] + ": " + num2[2])
		numx +=1
		prevfinal.append(prevorg2)
		prevorg2 = ''

	return render(request, 'index.html', {'prev': prevfinal} )

#def ClimaParqueRender(request):
#	return render(request, 'index.html')

