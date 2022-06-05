import sys
import os
sys.path.append(os.getcwd())

from complx_num_algbra.calculator import *

'''Run this file from the parent directory with "pytest test_files\tests_real_complx_subs.py" '''

def test_real_complx_subs_1():
    result = real_complx_subs('4+8i', '5+10i')
    assert result == '-1-2i'

def test_real_complx_subs_2():
    result = real_complx_subs('5+10i', '4+8i')
    assert result == '1+2i'

def test_real_complx_subs_3():
    result = real_complx_subs('5+10i', '4-8i')
    assert result == '1+18i'

def test_real_complx_subs_4():
    result = real_complx_subs('4-8i', '5+10i')
    assert result == '-1-18i'

def test_real_complx_subs_5():
    result = real_complx_subs('5', '4-8i')
    assert result == '1+8i'

def test_real_complx_subs_6():
    result = real_complx_subs('4-8i', '5')
    assert result == '-1-8i'

def test_real_complx_subs_7():
    result = real_complx_subs('4-8i', '0')
    assert result == '4-8i'

def test_real_complx_subs_8():
    result = real_complx_subs('0', '4-8i')
    assert result == '-4+8i'