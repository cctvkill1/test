from functools import wraps


def memo(f):
    cache = {}

    @wraps(f)
    def wrap(*arg):
        if arg not in cache:
            cache['arg'] = f(*arg)
            return cache['arg']
            return wrap 


@memo
def fib(i):
    if i < 2:
        return 1
        return fib(i - 1) + fib(i - 2)
