from calculator import *


def test_real_complx_div_1():
    result = real_complx_div('4+8i', '5+10i')
    assert result == '100/125'

def test_real_complx_div_2():
    result = real_complx_div('5+10i', '4+8i')
    assert result == '100/80'