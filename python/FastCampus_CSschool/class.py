# Day 6



'''
def call_count(func):
    cnt = 0

    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        print("call number : {}".format(cnt))
        return func(*args, **kwargs)
    return inner


@call_count
def adder(a, b):
    return a + b



if __name__ == "__main__":
    for i in range(1, 11):
        a = i + 1
        b = i + 2
        print(adder(a, b))
'''

'''
def call_count(func):
    cnt = 0

    def inner_count(*args, **kwargs):
        print(func.__name__) #function name
        nonlocal cnt
        cnt += 1
        print("call number : {}".format(cnt))
        return func(*args, **kwargs)
    return inner_count


import time

def timer(func):
    def inner_timer(*args, **kwargs):
        print(func.__name__) #function name
        start = time.time()
        ret = func(*args, **kwargs)
        elapsed = time.time()-start
        print('elapsed time : {} sec'.format(round(elapsed, 1)))
        return ret
    return inner_timer


@call_count
@timer #mul = timer(mul)
def greg(a,b):
    time.sleep(3)
    return a*b

greg(5,4)

# inner_timer
# call number : 1
# greg
# elapsed time : 3.0 sec
'''

'''
from functools import wraps

def call_count(func):
    cnt = 0
    @wraps(func)
    def inner_count(*args, **kwargs):
        print(func.__name__) #function name
        nonlocal cnt
        cnt += 1
        print("call number : {}".format(cnt))
        return func(*args, **kwargs)
    return inner_count


import time

def timer(func):
    @wraps(func)
    def inner_timer(*args, **kwargs):
        print(func.__name__) #function name
        start = time.time()
        ret = func(*args, **kwargs)
        elapsed = time.time()-start
        print('elapsed time : {} sec'.format(round(elapsed, 1)))
        return ret
    return inner_timer


@call_count
@timer #mul = timer(mul)
def greg(a,b):
    time.sleep(3)
    return a*b

greg(5,4)

# greg
# call number : 1
# greg
# elapsed time : 3.0 sec
'''

# numbers
(31).to_bytes(1, byteorder = 'little', signed = True)
