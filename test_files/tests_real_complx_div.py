import sys
import os
sys.path.append(os.getcwd())

from complx_num_algbra.calculator import *

'''Run this file from the parent directory with "pytest test_files\tests_real_complx_div.py" '''

def test_real_complx_div_1():
    result = real_complx_div('4+8i', '5+10i')
    assert result == '(100/125)'

def test_real_complx_div_2():
    result = real_complx_div('5+10i', '4+8i')
    assert result == '(100/80)'

def test_real_complx_div_3():
    result = real_complx_div('4+8i', '4-8i')
    assert result == '-(48/80)+(64/80)i'

def test_real_complx_div_4():
    result = real_complx_div('4-8i', '4+8i')
    assert result == '-(48/80)-(64/80)i'