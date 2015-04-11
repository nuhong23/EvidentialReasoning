

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
        print(frame1)
        print(frame2)

        print('\n')

        value = []
        for i in relations1:
            for j in relations2:
                key = frame1[4] + ' v ' + str(j)
                value = float(frame1[3])
                self.translatedFrame1[key] = value
            theta = 1 - float(frame1[3])
            key = "theta"
            self.translatedFrame1[key] = theta

            key = frame2[4] + ' v ' + str(i)
            value = float(frame2[3])

        self.translatedFrame2[key] = value
        theta = 1 - float(frame2[3])
        key = "theta"
        self.translatedFrame2[key] = theta

        print(self.translatedFrame1)
        print(self.translatedFrame2)

        return self.translatedFrame1, self.translatedFrame2


    # Dempster's combination rule
    def fuse(self,translatedFrame1, translatedFrame2):
        pass

    def interpret(self):
        pass
