class Hyp_num:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __eq__(self,obj):
        if obj==None:
            return False
       # if not isinstance(obj.Hyp_num):
       #    return False
        return (self.x==obj.x) and (self.y==obj.y)
    
    def __ne__(self,obj):
        return not self==obj

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
        result.x = self.x*factor.x + self.y*factor.y
        result.y = self.x*factor.y + self.y*factor.x
        return result

    def modulus(self):
        """
        Determines the modulus of the hyperbolic number.
        """
        return self.x*self.x-self.y*self.y