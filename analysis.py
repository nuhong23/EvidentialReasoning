import numpy as np

# a = np.array([1,0,0])
#b = np.array([0,1,0])
#print np.cross(a,b)

class Analysis:

    def __init__(self):
        pass

    def discount(self, alpha, mass):
        try:
            return alpha * mass

        except ArithmeticError:
            print("Method can only multiply numbers and not string values.")
            print("Alpha and mass must be a numerical value")
            self.discount()

    def translate(self, parentFrame, childFrame, frameInfo, propositions):
        pass


    # Dempster's combination rule
    def fuse(self,str, massA, massB):

        if str.startswith("dependent"):
            return massA * massB

        if str.startswith("independent"):
            k = massA * massB
            return 1/(1-k)

    def interpret(self):
        pass