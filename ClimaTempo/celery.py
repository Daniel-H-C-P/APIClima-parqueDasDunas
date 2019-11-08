# APIClima-parqueDasDunas/ClimaTempo/celery.py

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
import requests
import time

'''
from celery.schedules import crontab
##############
import requests
import time
climaAgora = requests.get('https://api.openweathermap.org/data/2.5/weather?id=3394023&lang=pt&APPID=9e70fbffdde1b3cfcb57ddd5f3a250b4').json()
clima5dias = requests.get('https://api.openweathermap.org/data/2.5/forecast?id=3394023&lang=pt&APPID=9e70fbffdde1b3cfcb57ddd5f3a250b4').json()
##############
'''

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ClimaTempo.settings')

app = Celery('ClimaTempo')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


#@app.task(bind=True)
#def debug_task(self):
#    print('Request: {0!r}'.format(self.request))


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


@app.task
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

	print('pesquisa completa!')

'''