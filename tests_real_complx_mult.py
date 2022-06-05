from calculator import *

def test_real_complx_mult_1():
    result = real_complx_mult('4+8i', '5+10i')
    assert result == '-60+80i'

def test_real_complx_mult_2():
    result = real_complx_mult('4+8i', '5+10i')
    assert result == '-60+80i'

def test_real_complx_mult_3():
    result = real_complx_mult('4-8i', '5+10i')
    assert result == '100'

def test_real_complx_mult_4():
    result = real_complx_mult('5+10i', '4-8i')
    assert result == '100'

def test_real_complx_mult_5():
    result = real_complx_mult('4-8i', '5')
    assert result == '20-40i'

def test_real_complx_mult_6():
    result = real_complx_mult('4-8i', '0')
    assert result == '0'

def test_real_complx_mult_7():
    result = real_complx_mult('0', '4-8i')
    assert result == '0'