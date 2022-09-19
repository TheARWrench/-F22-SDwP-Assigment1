import sys
import os
import traceback
import datetime


def error_test(func):
    def wrap(*args,**kwargs):
        try:
            sys.stdout = open(os.devnull, 'w') 
            result = func(*args, **kwargs)
            sys.stdout = sys.__stdout__ 
            return result
        except:
            with open('./task4/err.log', 'a') as file:
                file.write('Exeption happened at '+str(datetime.datetime.now())+'\n')
                file.write('{}\n'.format(traceback.format_exc()))
    return wrap

class error_test_class:
    def __init__(self,f):
        self.f=f

    def __call__(self,*args,**kwargs):
        try:
            sys.stdout = open(os.devnull, 'w') 
            result = self.f(*args, **kwargs)
            sys.stdout = sys.__stdout__ 
            return result
        except:
            with open('./task4/err.log', 'a') as file:
                file.write('Exeption happened at '+str(datetime.datetime.now())+'\n')
                file.write('{}\n'.format(traceback.format_exc()))
