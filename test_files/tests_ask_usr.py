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

def test_is_input_wrong_8():
    result = is_input_wrong('1i+(1+5)')
    assert result == True

def test_is_input_wrong_9():
    result = is_input_wrong('1+5i')
    assert result == False

def test_is_input_wrong_10():
    result = is_input_wrong('1+(5/6)i')
    assert result == False

def test_is_input_wrong_11():
    result = is_input_wrong('(7/8)+(5/6)i')
    assert result == False

def test_is_input_wrong_12():
    result = is_input_wrong('(7/8i)+(5/6)i')
    assert result == True

def test_is_input_wrong_13():
    result = is_input_wrong('(7/8)i+(5/6)i')
    assert result == True

def test_is_input_wrong_14():
    result = is_input_wrong('(7/8)+(5/6)')
    assert result == True

def test_is_input_wrong_15():
    result = is_input_wrong('5+6')
    assert result == True

def test_is_input_wrong_16():
    result = is_input_wrong('(7/8)i+(5/6)')
    assert result == True

def test_is_input_wrong_17():
    result = is_input_wrong('(7)+(5/6)i')
    assert result == False

def test_is_input_wrong_18():
    result = is_input_wrong('(i)+(5/6)i')
    assert result == True

def test_is_input_wrong_19():
    result = is_input_wrong('-(5/6)i')
    assert result == False

def test_is_input_wrong_20():
    result = is_input_wrong('-(5/6)')
    assert result == False

def test_is_input_wrong_21():
    result = is_input_wrong('-(5/6)+')
    assert result == True

def test_is_input_wrong_22():
    result = is_input_wrong('-(5/6)+i')
    assert result == False

def test_is_input_wrong_22():
    result = is_input_wrong('i-(5/6)')
    assert result == True

def test_is_input_wrong_23():
    result = is_input_wrong('(5.1/6)-i')
    assert result == True

''' Other wrong formats that should not pass
    - 1i+(1+5)
    '''

if __name__ == '__main__':
    os.chdir('..') # For being able to debug while testing
    sys.exit(pytest.main(['-k', 'tests_ask_usr.py'], plugins=[test_is_input_wrong_23()]))