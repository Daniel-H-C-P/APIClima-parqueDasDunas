import datetime
###################### 1 #####################
#leitura dos arquivos json
import json 
#Para abrir o arquivo climaAgora
def climanow():
	with open('/home/daniel/webdev/tcc2019/APIClima-parqueDasDunas/ClimaTempo/climaAgora.json') as f:
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
	with open('/home/daniel/webdev/tcc2019/APIClima-parqueDasDunas/ClimaTempo/clima5dias.json') as g:
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
		
	dia_hoje = 'Dia {}: '.format(prevorganizada[0][0][0])
	for num1 in prevorganizada[0]:
		dia_hoje += ' ' + (num1[1] + ": " + num1[2] +',')
	
	#print (dia_hoje)
	return dia_hoje
	
#prevhoje()


#################### 2 ####################
# Mandar email
climatual = climanow()
prevclima = prevhoje()

import smtplib
from minhachaveOW import meuemail, minhasenha
def mandaemail(nome, contato, dia, hora, climatual, prevclima):
	meu_email = meuemail
	minha_s = minhasenha
	#climatual = climanow()
	#prevclima = prevhoje()


	with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
		smtp.ehlo()
		smtp.starttls()
		smtp.ehlo()

		smtp.login(meu_email, minha_s)

		assunto = 'Alerta climático'
		corpo = 'Olá, {}!\n Esta é a previsão para o Parque das Dunas após seu alerta({} - {}):\n Clima Atual -> {}.\n Previsão -> {}.\n Esperamos que tenha uma boa trilha!\n Equipe ClimaTempo'.format(nome, dia, hora, climatual, prevclima)

		mensagem = f'Subject: {assunto}\n\n{corpo}'

		smtp.sendmail( meu_email, contato, mensagem.encode('utf-8'))

# mandaremail("Daniel", "dhcp2013@gmail.com", "hoje2", "agora2")





#Para mudar de pasta
import os
# print(os.path.abspath(os.curdir)) #só pra checar o dir base
os.chdir('/home/daniel/webdev/tcc2019/APIClima-parqueDasDunas/')
# print(os.path.abspath(os.curdir)) #só pra checar o dir acima
##########################################
'''
Para ler diretamente dos modelos:

from cadastro.models import EmailCliente

pessoas = EmailCliente.objects.all()

print (pessoas)

'''
#########################################
#Parte que lê o bd em sqlite3:

import sqlite3

conn = sqlite3.connect('db.sqlite3') #cria a conexão

c = conn.cursor() #permite fazer operações no banco

c.execute("SELECT * FROM cadastro_emailcliente WHERE mandado=0 ") #execute -> sql

lista = c.fetchall() #busca todos os resultados e cria uma lista

for pessoa in lista:
    #print(pessoa)
    #print(pessoa[0]) #id
    #print(pessoa[1]) #nome
    #print(pessoa[2]) #contato
    #print(pessoa[3]) #dia
    #print(pessoa[4]) #hora
    alerta = pessoa[3] + ' ' + pessoa[4]
    alerta = datetime.datetime.strptime(alerta, "%Y-%m-%d %H:%M:%S")
    if datetime.datetime.now() >= alerta:
    	mandaemail(pessoa[1],pessoa[2],pessoa[3],pessoa[4], climatual, prevclima)
    ############################## ESTAS DUAS LINHAS MUDAM O BD PELO ID DO OBJETO!!!!
    	c.execute('UPDATE cadastro_emailcliente SET mandado = 1 WHERE id = {}'.format(int(pessoa[0])))
    	conn.commit()
    ############################## 



    #comando loop para interagir com os emails
    #pegar nome, contato, dia, hora e interagir com mandarEmail

#conn.commit() # comete as alterações na tabela

c.close() # fecha a coneção 1
conn.close() # fecha a coneção 2
