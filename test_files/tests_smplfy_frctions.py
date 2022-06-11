import sys
import os
sys.path.append(os.getcwd())
from calculator import *
import pytest

'''Run this file from the parent directory with "pytest test_files\tests_smplfy_frctions.py" '''

def test_smplfy_frctions_1():
    uppr_part, lwr_part = 8, 12
    uppr_part, lwr_part = smplfy_frctions(uppr_part, lwr_part)
    assert uppr_part == 2
    assert lwr_part == 3

def test_smplfy_frctions_2():
    uppr_part, lwr_part = 25, 50
    uppr_part, lwr_part = smplfy_frctions(uppr_part, lwr_part)
    assert uppr_part == 1
    assert lwr_part == 2

def test_smplfy_frctions_3():
    uppr_part, lwr_part = 6, 12
    uppr_part, lwr_part = smplfy_frctions(uppr_part, lwr_part)
    assert uppr_part == 1
    assert lwr_part == 2

if __name__ == '__main__':
    os.chdir('..') # For being able to debug while testing
    sys.exit(pytest.main(['-k', 'tests_smplfy_frctions.py'], plugins=[test_smplfy_frctions_1()]))