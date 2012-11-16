from celery import Celery

celery = Celery('tasks', broker='redis://localhost')


@celery.task
def fib(n):
    if n > 1:
        return fib(n - 1) + fib(n - 2)
    else:
        return 1
