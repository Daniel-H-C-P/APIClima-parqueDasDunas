# ApiClima.../ClimaTempo/tasks.py

from celery import Celery, shared_task

@shared_task
#@app.task
def adding_task(x, y):
    return x + y