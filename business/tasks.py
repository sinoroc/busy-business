""" Business tasks
"""


import celery
import time


app = celery.Celery('business.tasks')


@app.task
def foo(counter):
    print("Executing task foo...")
    for i in range(0, counter):
        print("Foo [{}]".format(i))
        time.sleep(1)
    return i + 1


@app.task
def foo_callback(result):
    print("Task foo successfully executed. Result: [{}].".format(result))
    return None


@app.task
def bar():
    print("Executing task bar...")
    return None


# EOF
