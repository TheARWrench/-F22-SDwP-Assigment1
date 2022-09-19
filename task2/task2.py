import time

def decorator(f):
    callCount={}
    def wrap(*args, **kwargs):
        time1 = time.time()
        if f.__name__ in callCount:
            callCount[f.__name__]+=1
        else:
            callCount[f.__name__]=1
        ret = f(*args, **kwargs)
        time2 = time.time()
        print('Function '+f.__name__+' called ' + str(callCount[f.__name__]) +
              ' time and it take ' + str((time2-time1)*1000.0)+" ms")
        print("Now it\'s properties")
        print
        return ret
    return wrap