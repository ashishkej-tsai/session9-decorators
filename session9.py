def run_only_odd_sec(fn):
    from datetime import datetime
    def inner(*args, **kwargs):
        if (datetime.now().time().second % 2) == 1:
            return fn(*args, **kwargs)
        else:
            print('Current time is even seconds')
    return inner

@run_only_odd_sec
def add(a,b):
    '''
    Add two numbers only when seconds is odd
    '''
    return a+b

def logged(fn):
    from functools import wraps
    from datetime import datetime, timezone
    @wraps(fn)
    def inner(*args, **kwargs):
        run_dt = datetime.now().date()
        result = fn(*args, **kwargs)
        print(f'{run_dt}: called {fn.__name__} with result {result}')
        return result
    return inner

@logged
def mult(a,b):
    '''
    Multiply two numbers, log the timezone when it is called
    '''
    return a*b

def set_password():
    '''
    Set initial Password
    '''
    password = ''
    def inner():
        nonlocal password
        if password == '':
            password = input()
        return password
    return inner

def authenticate(current_password, user_password):
    '''
    Decorator factory
    '''
    def inner_1(fn):
        cnt = 0
        if user_password == current_password:
            def inner(*args, **kwargs):
                nonlocal cnt
                cnt += 1
                print(f'{fn.__name__} was called {cnt} times')
                return fn(*args, **kwargs)
            return inner
        else:
            print('You scamster!!')
    return inner_1


def calc_fib_recurse(n):
    return 1 if n < 3 else calc_fib_recurse(n-2) + calc_fib_recurse(n-1)

def timed(reps):
    def inner_1(fn):
        from time import perf_counter
        def inner(*args, **kwargs):
            total_elapsed = 0
            for i in range(reps):
                start = perf_counter()
                result = fn(*args, **kwargs)
                end = perf_counter()
                total_elapsed += (end - start)
            avg_run_time = total_elapsed / reps
            print('Avg Run time: {0:.6f}s ({1} reps)'.format(avg_run_time, reps))
            return result
        return inner
    return inner_1

@timed(15)
def fib(n):
    return calc_fib_recurse(n)

from functools import singledispatch

@singledispatch
def htmlize(a):
    return escape(str(a))

@htmlize.register(int)
def html_int(a):
    return f'{a}(<i>{str(hex(a))}</i>)'

@htmlize.register(float)
def html_real(a):
    return f'{round(a, 2)}'

from decimal import Decimal
@htmlize.register(Decimal)
def html_real(a):
    return f'{round(a, 2)}'

def html_escape(arg):
    return escape(str(arg))

@htmlize.register(str)
def html_str(s):
    return html_escape(s).replace('\n', '<br/>\n')

@htmlize.register(tuple)
@htmlize.register(list)
def html_sequence(l):
    items = (f'<li>{html_escape(item)}</li>' for item in l)
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

@htmlize.register(dict)
def html_dict(d):
    items = (f'<li>{k}={v}</li>' for k, v in d.items())
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'