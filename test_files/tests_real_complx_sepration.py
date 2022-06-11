import sys
import os
sys.path.append(os.getcwd())

from complx_num_algbra.calculator import *

'''Run this file from the parent directory with "pytest test_files\tests_real_complx_sepration.py" '''

def test_real_complx_sepration_1():
    real_prt1, complx_prt1 = real_complx_sepration('4-8i')
    assert real_prt1 == '4'
    assert complx_prt1 == '-8'

def test_real_complx_sepration_2():
    real_prt1, complx_prt1 = real_complx_sepration('4+8i')
    assert real_prt1 == '4'
    assert complx_prt1 == '8'

def test_real_complx_sepration_3():
    real_prt1, complx_prt1 = real_complx_sepration('-4-8i')
    assert real_prt1 == '-4'
    assert complx_prt1 == '-8'

def test_real_complx_sepration_4():
    real_prt1, complx_prt1 = real_complx_sepration('+4-8i')
    assert real_prt1 == '4'
    assert complx_prt1 == '-8'

def test_real_complx_sepration_5():
    real_prt1, complx_prt1 = real_complx_sepration('+0-8i')
    assert real_prt1 == '0'
    assert complx_prt1 == '-8'

def test_real_complx_sepration_6():
    real_prt1, complx_prt1 = real_complx_sepration('+0-0i')
    assert real_prt1 == '0'
    assert complx_prt1 == '0'

def test_real_complx_sepration_7():
    real_prt1, complx_prt1 = real_complx_sepration('+0')
    assert real_prt1 == '0'
    assert complx_prt1 == '0'

def test_real_complx_sepration_8():
    real_prt1, complx_prt1 = real_complx_sepration('-0.0000i')
    assert real_prt1 == '0'
    assert complx_prt1 == '0'

def test_real_complx_sepration_9():
    real_prt1, complx_prt1 = real_complx_sepration('-3.45+53213.676i')
    assert real_prt1 == '-3.45'
    assert complx_prt1 == '53213.676'

def test_real_complx_sepration_10():
    real_prt1, complx_prt1 = real_complx_sepration('0+16i')
    assert real_prt1 == '0'
    assert complx_prt1 == '16'

def test_real_complx_sepration_11():
    real_prt1, complx_prt1 = real_complx_sepration('-0-8i')
    assert real_prt1 == '0'
    assert complx_prt1 == '-8'

def test_real_complx_sepration_12():
    real_prt1, complx_prt1 = real_complx_sepration('-8-0i')
    assert real_prt1 == '-8'
    assert complx_prt1 == '0'

def test_real_complx_sepration_13():
    real_prt1, complx_prt1 = real_complx_sepration('-(8/12)-(9/4)i')
    assert real_prt1 == '-(8/12)'
    assert complx_prt1 == '-(9/4)'

def test_real_complx_sepration_14():
    real_prt1, complx_prt1 = real_complx_sepration('+(8/12)+(9/4)i')
    assert real_prt1 == '(8/12)'
    assert complx_prt1 == '(9/4)'

def test_real_complx_sepration_15():
    real_prt1, complx_prt1 = real_complx_sepration('+(8/12)+0i')
    assert real_prt1 == '(8/12)'
    assert complx_prt1 == '0'

def test_real_complx_sepration_16():
    real_prt1, complx_prt1 = real_complx_sepration('+0+(9/4)i')
    assert real_prt1 == '0'
    assert complx_prt1 == '(9/4)'