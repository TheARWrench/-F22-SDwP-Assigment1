import time
import inspect


class decorator_3_2:
    global callCount
    callCount = {}

    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        time1 = time.time()
        if self.f.__name__ in callCount:
            callCount[self.f.__name__] += 1
        else:
            callCount[self.f.__name__] = 1
        ret = self.f(*args, **kwargs)
        time2 = time.time()
        with open("./task3/dec32.txt", 'a') as file:
            file.write('\nFunction '+self.f.__name__+' called ' + str(callCount[self.f.__name__]) +
                       ' time and it take ' + str((time2-time1)*1000.0)+" ms")
            file.write("\nNow properties\nfunc name:"+str(self.f.__name__)+"\nType :"+str(type(self.f))+"\nSign : "+str(inspect.signature(self.f)) +
                       '\nPos args: '+str(args)+'\nKeyworded args: '+str(kwargs)+"\nDoc: "+str(self.f.__doc__)+'\nSource: '+str(inspect.getsource(self.f))+'\nOutput: '+str(self.f(*args)))
        return ret


class decorator_3_1:
    global callCount
    callCount = {}

    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        time1 = time.time()
        if self.f.__name__ in callCount:
            callCount[self.f.__name__] += 1
        else:
            callCount[self.f.__name__] = 1
        ret = self.f(*args, **kwargs)
        time2 = time.time()
        with open("./task3/dec31.txt", 'a') as file:
            file.write('\nFunction '+self.f.__name__+' called ' + str(callCount[self.f.__name__]) +
                       ' time and it take ' + str((time2-time1)*1000.0)+" ms")

        return ret


def spidtest(*args):
    ranking = {}
    for i in args:
        time1 = time.time()
        i()
        time1_1 = time.time()
        ranking[i.__name__] = (time1_1-time1)*1000
    ranking = sorted(ranking.items(), key=lambda item: item[1])
    file = open('./task3/spidtest.txt','a')
    file.write(("{:<10}|{:<10}|{:<10}".format(*["PROGRAM", "RANK", "TIME ELAPSED"])+'\n'))
    temp = []
    for name, times in ranking:
        temp.append(name)
        file.write("{:<10}|{:<10}|{:<10.10f} ms".format(
            name, temp.index(name) + 1, times)+'\n')
