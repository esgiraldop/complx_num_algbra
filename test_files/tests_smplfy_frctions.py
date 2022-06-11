import sys
import os
os.chdir('..')
sys.path.append(os.getcwd())

from calculator import *

import pytest

def test_smplfy_frctions_1():
    uppr_part, lwr_part = 8, 12
    uppr_part, lwr_part = smplfy_frctions(uppr_part, lwr_part)
    assert uppr_part == 2
    assert lwr_part == 3

if __name__ == '__main__':
    sys.exit(pytest.main(['-k', 'tests_smplfy_frctions.py'], plugins=[test_smplfy_frctions_1()()]))