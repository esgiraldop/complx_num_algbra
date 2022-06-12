import sys
import os
sys.path.append(os.getcwd())
from ask_usr import *
import pytest

'''Run this file from the parent directory with "pytest test_files\tests_ask_usr.py" '''

def test_is_input_wrong_1():
    result = is_input_wrong('1+ i')
    assert result == True

def test_is_input_wrong_2():
    result = is_input_wrong('1+ii')
    assert result == True

def test_is_input_wrong_3():
    result = is_input_wrong('(1)+(i')
    assert result == True

def test_is_input_wrong_4():
    result = is_input_wrong('-(1)++i')
    assert result == True

def test_is_input_wrong_5():
    result = is_input_wrong('-1+e')
    assert result == True

def test_is_input_wrong_6():
    result = is_input_wrong('1+(1+5i)')
    assert result == True

def test_is_input_wrong_7():
    result = is_input_wrong('1+(1+5)i')
    assert result == True

''' Other wrong formats that should not pass
    - 1i+(1+5)
    '''

if __name__ == '__main__':
    os.chdir('..') # For being able to debug while testing
    sys.exit(pytest.main(['-k', 'tests_ask_usr.py'], plugins=[test_is_input_wrong_5()]))