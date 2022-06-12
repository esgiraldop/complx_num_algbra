import sys
import os
sys.path.append(os.getcwd())
from calculator import *
import pytest

'''Run this file from the parent directory with "pytest test_files\tests_real_complx_div.py" '''

def test_real_complx_div_1():
    result = real_complx_div('4+8i', '5+10i')
    assert result == '(4/5)'

def test_real_complx_div_2():
    result = real_complx_div('5+10i', '4+8i')
    assert result == '(5/4)'

def test_real_complx_div_3():
    result = real_complx_div('4+8i', '4-8i')
    assert result == '-(3/5)+(4/5)i'

def test_real_complx_div_4():
    result = real_complx_div('4-8i', '4+8i')
    assert result == '-(3/5)-(4/5)i'

def test_real_complx_div_5():
    result = real_complx_div('0', '4+8i')
    assert result == '0'

def test_real_complx_div_6():
    result = real_complx_div('4+8i', '4+8i')
    assert result == '1'

if __name__ == '__main__':
    os.chdir('..') # For being able to debug while testing
    sys.exit(pytest.main(['-k', 'tests_real_complx_div.py'], plugins=[test_real_complx_div_4()]))