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


    def translate(self, frame1,frame2):
        pass

    def fuse(self):
        pass
    
    def interpret(self):
        pass