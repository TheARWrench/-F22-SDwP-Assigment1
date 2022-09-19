import time
import inspect


def decorator_2(f):
    callCount = {}

    def wrap(*args, **kwargs):
        time1 = time.time()
        if f.__name__ in callCount:
            callCount[f.__name__] += 1
        else:
            callCount[f.__name__] = 1
        ret = f(*args, **kwargs)
        time2 = time.time()
        print('Function '+f.__name__+' called ' + str(callCount[f.__name__]) +
              ' time and it take ' + str((time2-time1)*1000.0)+" ms")
        print("Now properties\nfunc name:"+str(f.__name__)+"\nType :"+str(type(f))+"\nSign : "+str(inspect.signature(f)) +
              '\nPos args: '+str(args)+'\nKeyworded args: '+str(kwargs)+"\nDoc: "+str(f.__doc__)+'\nSource: '+str(inspect.getsource(f))+'\nOutput: '+str(f(*args)))

        return ret
    return wrap
