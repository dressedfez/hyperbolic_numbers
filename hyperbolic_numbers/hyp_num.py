class Hyp_num:
    def __init__(self,x,y):
        self.x = x
        self.y = y

def add(self, summand):
    """
    Add the summand to the hyperbolic number.
    """
    result = Hyp_num(0,0)
    result.x = self.x + summand.x
    result.y = self.y + summand.y
    return result

def multiply(self, factor):
    """
    Multiply the factor with the hyperbolic number.
    """
    result = Hyp_num(0,0)
    result.x = self.x*factor.y + self.y*factor.y
    result.y = self.x*factor.y + self.y*factor.x
    return result