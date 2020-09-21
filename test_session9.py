import subprocess
import sys
import random
from datetime import datetime
import pytest
import session9
from session9 import add, mult, set_password, authenticate, calc_fib_recurse, fib, timed, htmlize
import time
import os.path
import re
import inspect 

README_CONTENT_CHECK_FOR = [
    'decorator',
    'factory'
]

def test_odd_secs():
	if (datetime.now().time().second % 2) == 1:
		assert add(1,2) == 3, "func add not working in odd seconds"

def test_logged():
	assert mult(3,4) == 12, "func mult not logged"

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_authenticate():
	current_pass = 'Ashish'
	@authenticate(current_pass,'Ashish')
	def div(a,b):
		return a/b
	assert div(4,2) == 2, "authenticate not working"

def test_timed():
	assert fib(2) == 1, "timed not working"

def test_htmlize():
	assert htmlize(100) == '100(<i>0x64</i>)', "htmlize is not working"

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
    lines = inspect.getsource(session9)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert re.search('[a-zA-Z#@\'\"]', space), "Your code intentation does not follow PEP8 guidelines"
        assert len(re.sub(r'[a-zA-Z#@\n\"\']', '', space)) % 4 == 0, \
        "Your code intentation does not follow PEP8 guidelines"

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session9, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

