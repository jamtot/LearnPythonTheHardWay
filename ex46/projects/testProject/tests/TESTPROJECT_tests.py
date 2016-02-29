from nose.tools import *
from TESTPROJECT.weightChecker import WeightChecker

def test_checker():

    tChecker = WeightChecker('/home/jamtot/Python/LrnPython/ex46/projects/testProject/tests/file_test.txt')

    for line in tChecker.weightLines:
        assert_equal(len(line), 15)
