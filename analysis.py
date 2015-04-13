

class Analysis:

    translatedFrame1 = {}
    translatedFrame2 = {}
    insertFrame = []
    newRelations = []

    def __init__(self):
        pass


    def discount(self, alpha, mass):
        try:
            print("Entered discount operation")
            alpha = float(alpha)
            mass = float(mass)

            if alpha >= 1 or alpha <= 0:
                self.discount(alpha, mass)
                print("The number must be between 0 and 1.")
            else:
                self.discounted = float(alpha) * float(mass)
                return self.discounted

        except (TypeError,ValueError):
            print("Must be a number and not a string.")
            self.discount(alpha, mass)



    def translate(self,frame1, relations1, frame2, relations2):
        print("printing in translating\n")

        value = []

        length_ofFrame1 = len(frame1)
        length_ofFrame2 = len(frame2)

        x = 3
        y = 3
        theta = 0
        theta2 = 0

        while x < length_ofFrame1:
            while y < length_ofFrame2:
                for i in relations1:
                    for j in relations2:
                        key = frame1[x + 1] + ' v ' + str(j)
                        value = float(frame1[x])
                        self.translatedFrame1[key] = value

                        theta = 1 - value - theta
                        key = "theta"
                        self.translatedFrame1[key] = theta

                        print(self.translatedFrame1)

                    key2 = frame2[y + 1] + ' v ' + str(i)
                    value2 = float(frame2[y])

                self.translatedFrame2[key2] = value2

                theta2 = 1 - value2 - theta2
                key = "theta"
                self.translatedFrame2[key] = theta2

                print(self.translatedFrame2)
                y = y + 2
            print(y)
            x = x + 2
        print(x)

        return self.translatedFrame1, self.translatedFrame2


    # Dempster's combination rule
    def fuse(self,translatedFrame1, translatedFrame2):
        pass

    def interpret(self):
        pass
