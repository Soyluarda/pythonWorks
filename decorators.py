from time import *
import random

def timer(function):
    def f(*args,**kwargs):
        before_time = time()
        function(*args,**kwargs)
        after_time = time()
        print ("function takes time:",after_time - before_time)
    return f

@timer
def function1(wait_time):
    wait  = random.randint(1,10)
    print ("we try to find wait time, I guess it's ", wait_time)
    print ("wait time is....  ", wait )


function1(15)
