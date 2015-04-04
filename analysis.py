
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

    def translate(self,Frame1,relations1,Frame2, relations2):
        print("printing in translating\n")
        print(Frame1)
        print(relations1)
        print(Frame2)
        print(relations2)
        #splitter = relations1.split(',')
        #print(splitter)



    # Dempster's combination rule
    def fuse(self,translatedFrame):
        pass

    def interpret(self):
        pass