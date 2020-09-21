import subprocess
import sys
import random



import pytest
import session8
from session8 import add, mul, div, counter_local_dict, counter_global_dict, next_fibonacci, check_docstring, func_dict
import time
import os.path
import re
import inspect 

README_CONTENT_CHECK_FOR = [
    'Closure',
    'outer',
    'inner',
    'doc',
    'string',
    'free',
    'variable'
]

def test_check_docstring():
    fn = check_docstring()
    assert fn(check_docstring), "check_docstring function has greater than 50 characters "

def test_next_fibonacci():
    t = next_fibonacci()
    f = t()
    f = t()
    f = t()
    assert f == 2, "Third fibonacci number is 2"

def test_counter_global():
    counter_add, counter_mul, counter_div = counter_global_dict()
    counter_add(5,2)
    counter_div(5,2)
    counter_mul(5,2)
    assert func_dict ==  {'add':1, 'mul':1, 'div':1}, "Global dict add, mul, div called 1 time each"

def test_counter_local():
    local_dict_1 = {"add":0, "mul":0, "div":0}
    local_dict_2 = {"add":0, "mul":0, "div":0}
    counter_add_1, counter_mul_1, counter_div_1 = counter_local_dict(local_dict_1)
    counter_add_2, counter_mul_2, counter_div_2 = counter_local_dict(local_dict_2)
    counter_add_1(5,3)
    counter_div_2(4,5)
    assert local_dict_1 ==  {'add':1, 'mul':0, 'div':0}, "Local Dict 1 Add called 1 time"
    assert local_dict_2 ==  {'add':0, 'mul':0, 'div':1}, "Local Dict 2 Div called 1 time"

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r",encoding="utf-8")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r",encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r",encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

    
def test_fourspace():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session8)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert re.search('[a-zA-Z#@\'\"]', space), "Your code intentation does not follow PEP8 guidelines"
        assert len(re.sub(r'[a-zA-Z#@\n\"\']', '', space)) % 4 == 0, \
        "Your code intentation does not follow PEP8 guidelines"

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session8, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

