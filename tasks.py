import logging

from celery import Celery
from celery.task import periodic_task
from datetime import timedelta
from os import environ

REDIS_URL = environ.get('REDISTOGO_URL', 'redis://localhost')

celery = Celery('tasks', broker=REDIS_URL)


def fib(n):
    if n > 1:
        return fib(n - 1) + fib(n - 2)
    else:
        return 1


@periodic_task(run_every=timedelta(seconds=10))
def print_fib():
    logging.info(fib(30))
