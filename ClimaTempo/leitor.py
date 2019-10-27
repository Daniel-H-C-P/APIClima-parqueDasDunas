#arquivo teste para criar as views com a leitura dos arquivos json


import json 
#import re
 
#Para abrir o arquivo climaAgora
def climanow():
	with open('climaAgora.json') as f:
		data = json.load(f)
	#Lendo o arquivo
	climaatual = data['weather'][0]['description']
	#print('Clima atual:')
	#print(climaatual)
	return climaatual
#climanow()


#Para abrir o arquivo clima5dias
def climaprev():
	with open('clima5dias.json') as g:
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
	'''
	numx = 0
	for num1 in prevorganizada:
		print('\nDia {}'.format(prevorganizada[numx][0][0]))
		for num2 in num1:
			print(num2[1] + ": " + num2[2])
		numx+=1
	'''
	prevfinal = ''
	numx = 0
	for num1 in prevorganizada:
		prevfinal+= ('\n\nDia {}:'.format(prevorganizada[numx][0][0]))
		for num2 in num1:
			prevfinal+= '\n' + (num2[1] + ": " + num2[2])
		numx +=1

	#print("\nExemplo de exibição específica:")
	#print(prevorganizada[2][0][2])
	#print(prevfinal)
	return prevorganizada
#climaprev()

def prevhoje():
	with open('clima5dias.json') as g:
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

		#prevfinal = []
		#prevorg2 = ''
		#numx = 0
		#for num1 in prevorganizada:
		#	prevorg2+= ('Dia {}: '.format(prevorganizada[numx][0][0]))
		#	for num2 in num1:
		#		prevorg2+= (num2[1] + ": " + num2[2] + ' ')
		#	numx +=1
		#	prevfinal.append(prevorg2)
		#	prevorg2 = ''

	dia_hoje = 'Dia {}: '.format(prevorganizada[0][0][0])
	for num1 in prevorganizada[0]:
		dia_hoje += ' ' + (num1[1] + ": " + num1[2] +',')
	
	#print (dia_hoje)
	return dia_hoje
	
#prevhoje()