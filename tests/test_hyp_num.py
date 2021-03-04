from hyperbolic_numbers import hyp_num

class TestHyp_num():

    def test_add(self):
        expectedResult=hyp_num.Hyp_num(3, 5)
        a=hyp_num.Hyp_num(1, 2)
        b=hyp_num.Hyp_num(2, 3)
        result=a.add(b)
        assert expectedResult == result

    def test_multiply(self):
        expectedResult=hyp_num.Hyp_num(3, 5)
        a=hyp_num.Hyp_num(1, 2)
        b=hyp_num.Hyp_num(2, 3)
        result=a.multiply(b)
        assert expectedResult == result