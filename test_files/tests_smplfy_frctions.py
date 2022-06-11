import sys
import os
sys.path.append(os.getcwd())

from complx_num_algbra.calculator import *

'''Run this file from the parent directory with "pytest test_files\tests_smplfy_frctions.py" '''

def test_smplfy_frctions_1():
    uppr_part, lwr_part = 8, 12
    uppr_part, lwr_part = smplfy_frctions(uppr_part, lwr_part)
    assert uppr_part == 2
    assert lwr_part == 3