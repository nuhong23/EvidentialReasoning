

class Analysis:

    translatedFrame = {}

    def __init__(self):
        pass



    def discount(self, mass):
        alpha = input("What is the alpha number for adjustment? :")
        alpha = float(alpha)

        try:
            if alpha >= 1 or alpha <=0:
                self.discount(mass)
                print("The number must be between 0 and 1.")
            else:
                self.discounted = float(alpha) * float(mass)
                return self.discounted

        except TypeError:
            print("Must be a number and not a string.")
            self.discount(mass)



    def translate(self,frames):
        print("printing in translating\n")

        for i,k in frames:
            print (i,k)


    # Dempster's combination rule
    def fuse(self,translatedFrame):
        pass

    def interpret(self):
        pass
