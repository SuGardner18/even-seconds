from datetime import datetime
import time

def only_even_seconds (func):
    def wrapper (*args, **kwargs):
        seconds= datetime.now().second
        if seconds % 2 == 0:
            return func(*args, **kwargs)
    return wrapper

@only_even_seconds
def shout (message):
    print(message.upper())

for _ in range(20):
    shout("did I just decorate?")
    time.sleep(1)
