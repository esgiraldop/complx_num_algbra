from calculator import *

def test_real_complx_sum_1():
    result = real_complx_sum('4+8i', '5+10i')
    assert result == '9+18i'

def test_real_complx_sum_2():
    result = real_complx_sum('5+10i', '4+8i')
    assert result == '9+18i'

def test_real_complx_sum_3():
    result = real_complx_sum('5+10i', '4-8i')
    assert result == '9+2i'

def test_real_complx_sum_4():
    result = real_complx_sum('5', '4-8i')
    assert result == '9-8i'