#Para mudar de pasta
import os
print(os.path.abspath(os.curdir)) #só pra checar
os.chdir('..')
print(os.path.abspath(os.curdir)) #só pra checar

'''
Para ler diretamente dos modelos:

from cadastro.models import EmailCliente

pessoas = EmailCliente.objects.all()

print (pessoas)

'''

#Parte que lê o bd em sqlite3:

import sqlite3

conn = sqlite3.connect('db.sqlite3') #cria a conexão

c = conn.cursor() #permite fazer operações no banco

c.execute("SELECT * FROM cadastro_emailcliente WHERE mandado=0 ") #execute -> sql

lista = c.fetchall() #busca todos os resultados e cria uma lista

for pessoa in lista:
    print(pessoa)
    #comando loop para interagir com os emails
    #pegar nome, contato, dia, hora e interagir com mandarEmail

#conn.commit() # comete as alterações na tabela

c.close() # fecha a coneção 1
conn.close() # fecha a coneção 2





'''

COMO MUDAR VALORES EM SQLITE3:

UPDATE employees
SET lastname = 'Smith'
WHERE employeeid = 3;

'''


#Usar isso com num IF após enviar o email.