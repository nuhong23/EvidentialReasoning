
class Analysis:

    translatedFrame = []

    def __init__(self):
        pass

    def discount(self, alpha, mass):
        try:
            return alpha * mass

        except ArithmeticError:
            print("Method can only multiply numbers and not string values.")
            print("Alpha and mass must be a numerical value")
            self.discount()

    def translate(self,FOD1,FOD2):
        pass


    # Dempster's combination rule
    def fuse(self,translatedFrame):
        pass

    def interpret(self):
        pass