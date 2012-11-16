import logging

from celery import Celery
from datetime import timedelta

celery = Celery('tasks', broker='redis://localhost')

CELERYBEAT_SCHEDULE = {
    'every-ten-secs': {
        'task': 'tasks.print_fib',
        'schedule': timedelta(seconds=10),
        'args': (30),
    },
}


def fib(n):
    if n > 1:
        return fib(n - 1) + fib(n - 2)
    else:
        return 1


@celery.task
def print_fib(n):
    logging.info(fib(n))
