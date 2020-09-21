def check_docstring(n=50):
    '''
    Closure outer function to with n as free variable default value 50, number of charaters the doc string of function should have
    '''
    def inner_check(fn):
        '''
        Closure inner function to check whether the function fn has more than n=50 charaters doc string
        '''
        doc_string = fn.__doc__
        num_chars = len(doc_string)
        if num_chars > n:
            return True
        else:
            return False
    return inner_check

def next_fibonacci():
    '''
    Closure outer function to calculate the next fibonacci number
    '''
    cnt = 0
    num1 = 0
    num2 = 1
    def inner_fibonacci():
        '''
        Closure inner function to calculate the next fibonacci number
        '''
        nonlocal num1, num2,cnt
        if cnt == 0:
            cnt = 1
            return 1
        result = num1+num2
        num1 = num2
        num2 = result
        return result
    return inner_fibonacci

def add(a, b):
    return a + b
def mul(a, b):
    return a*b
def div(a,b):
    if b:
        return a/b
    else:
        return 0

func_dict = {"add":0, "mul":0, "div":0}

def counter_global_dict():
    '''
    Closure outer function for global dictionary func_dict
    '''
    cnt_add, cnt_mul, cnt_div = 0,0,0
    def inner_add(*args, **kwargs):
        '''
        Closure inner function to calculate number of times the add was called
        '''
        global func_dict
        nonlocal cnt_add
        cnt_add += 1
        func_dict["add"] = cnt_add
        print(f"Add: {func_dict['add']}, Mul: {func_dict['mul']}, Div: {func_dict['div']}")
        return add(*args, **kwargs)

    def inner_mul(*args, **kwargs):
        '''
        Closure inner function to calculate number of times the mul was called
        '''
        global func_dict
        nonlocal cnt_mul
        cnt_mul += 1
        func_dict["mul"] = cnt_mul
        print(f"Add: {func_dict['add']}, Mul: {func_dict['mul']}, Div: {func_dict['div']}")
        return mul(*args, **kwargs)

    def inner_div(*args, **kwargs):
        '''
        Closure inner function to calculate number of times the div was called
        '''
        global func_dict
        nonlocal cnt_div
        cnt_div += 1
        func_dict["div"] = cnt_div
        print(f"Add: {func_dict['add']}, Mul: {func_dict['mul']}, Div: {func_dict['div']}")
        return div(*args, **kwargs)

    return inner_add, inner_mul, inner_div


def counter_local_dict(dict_local):
    '''
    Closure outer function for local dictionary passed
    '''
    cnt_add, cnt_mul, cnt_div = 0,0,0
    def inner_add(*args, **kwargs):
        '''
        Closure inner function to calculate number of times the add was called
        '''
        nonlocal cnt_add
        cnt_add += 1
        dict_local["add"] = cnt_add
        print(f"Add: {dict_local['add']}, Mul: {dict_local['mul']}, Div: {dict_local['div']}")
        return add(*args, **kwargs)

    def inner_mul(*args, **kwargs):
        '''
        Closure inner function to calculate number of times the mul was called
        '''
        nonlocal cnt_mul
        cnt_mul += 1
        dict_local["mul"] = cnt_mul
        print(f"Add: {dict_local['add']}, Mul: {dict_local['mul']}, Div: {dict_local['div']}")
        return mul(*args, **kwargs)

    def inner_div(*args, **kwargs):
        '''
        Closure inner function to calculate number of times the div was called
        '''
        nonlocal cnt_div
        cnt_div += 1
        dict_local["div"] = cnt_div
        print(f"Add: {dict_local['add']}, Mul: {dict_local['mul']}, Div: {dict_local['div']}")
        return div(*args, **kwargs)

    return inner_add, inner_mul, inner_div


