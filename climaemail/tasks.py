


# ApiClima.../climaemail/tasks.py

from celery import Celery, shared_task, task
#from .funcoesback import pegaClima 
#from celery.schedules import crontab
##############
import requests
import time
climaAgora = requests.get('https://api.openweathermap.org/data/2.5/weather?id=3394023&lang=pt&APPID=9e70fbffdde1b3cfcb57ddd5f3a250b4').json()
clima5dias = requests.get('https://api.openweathermap.org/data/2.5/forecast?id=3394023&lang=pt&APPID=9e70fbffdde1b3cfcb57ddd5f3a250b4').json()
##############

'''
@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(300.0, pegaClima(), name='pega o clima')

    # Calls test('world') every 30 seconds
    sender.add_periodic_task(30.0, print('task 2 funcionando'))

    # Executes every Monday morning at 7:30 a.m.
    sender.add_periodic_task(
        crontab(minute='*/5'),
        print('task 2 funcionando'),
    )
'''

@task
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
	
'''
from celery import Celery
from celery.schedules import crontab

app = Celery()

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')

    # Calls test('world') every 30 seconds
    sender.add_periodic_task(30.0, test.s('world'), expires=10)

    # Executes every Monday morning at 7:30 a.m.
    sender.add_periodic_task(
        crontab(hour=7, minute=30, day_of_week=1),
        test.s('Happy Mondays!'),
    )

@app.task
def test(arg):
    print(arg)

'''