from calculator import *

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