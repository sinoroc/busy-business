""" Business tasks
"""


import billiard
import celery
import socket
import time


celery_app = celery.Celery('business.tasks', backend='redis://redis')

host_name = socket.gethostname()


@celery.task
def foo(counter):
    print("Executing task foo...")
    process = billiard.current_process()
    worker_name = process.initargs[1]
    process_index = process.index
    for i in range(0, counter):
        print("Foo [{}]".format(i))
        time.sleep(1)
    return {
        'host': host_name,
        'worker': worker_name,
        'process': process_index,
        'value': i + 1,
    }


@celery.task
def foo_callback(result):
    print("Task foo successfully executed. Result: [{}].".format(result))
    return None


@celery.task
def bar():
    print("Executing task bar...")
    return None


# EOF
