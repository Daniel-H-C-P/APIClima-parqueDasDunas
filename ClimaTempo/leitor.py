#arquivo teste para criar as views com a leitura dos arquivos json


import json 
 
#Para abrir o arquivo climaAgora
with open('climaAgora.json') as f:
  data = json.load(f)
 
#Lendo o arquivo
for clima in data['weather'][0]['description']:
    print(clima)

#Para abrir o arquivo clima5dias
with open('clima5dias.json') as g:
  data2 = json.load(g)
 
#Lendo o arquivo
previsao = ""
numheader = 0
while numheader < 40:
	climaprint = str(data2['list'][numheader]['dt_txt']) + " " + str(data2['list'][numheader]['weather'][0]['description'])  + '\n'
	previsao += climaprint
	numheader +=1
print(previsao)