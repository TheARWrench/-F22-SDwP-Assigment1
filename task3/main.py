from task3 import decorator_3_1
from task3 import decorator_3_2
from task3 import spidtest
import random
import time

@decorator_3_1
def func():
    time.sleep(random.uniform(0.0, 0.1))
        
@decorator_3_2
def funx():
    time.sleep(random.uniform(0.0, 0.1))

@decorator_3_2
def funh():
    time.sleep(random.uniform(0.0, 0.1))

def fun1():
    time.sleep(random.uniform(0.0, 0.1))

def fun2():
    time.sleep(random.uniform(0.0, 0.1))

def fun3():
    time.sleep(random.uniform(0.0, 0.1))

if __name__ == "__main__": 
    func()
    funx()
    funh()
    spidtest(fun1,fun2,fun3)