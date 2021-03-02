from hyperbolic_numbers import *

def test_add():
    expectedResult=Hyp_num(3, 5)
    a=Hyp_num(1, 2)
    b=Hyp_num(2, 3)
    result=a.add(b)
    assert expectedResult == result

def test_multiply():
    expectedResult=Hyp_num(3, 5)
    a=Hyp_num(1, 2)
    b=Hyp_num(2, 3)
    result=a.multiply(b)
    assert expectedResult == result