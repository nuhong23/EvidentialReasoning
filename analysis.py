

class Analysis:

    translatedFrame = {}
    newFrame = []
    newRelations = []

    def __init__(self):
        pass



    def discount(self, alpha, mass):
        try:
            alpha = float(alpha)
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
        key = frame1[0] + "x" + frame2[0]

        try:
            splitter1 = relations1.split(',')
            splitter2 = relations2.split(',')

            for i in splitter1:
                for j in splitter2:
                    string = i + ' v ' + j
                    value.append(string)
                    self.newRelations.append(string)

        except AttributeError:
            splitter2 = relations2.split(',')

            for i in relations1:
                for j in splitter2:
                    string = i + ' v ' + j
                    value.append(string)

        self.newFrame.append(key)
        self.translatedFrame[key] = value
        print(self.translatedFrame)
        return self.translatedFrame, self.newFrame, self.newRelations


    # Dempster's combination rule
    def fuse(self,translatedFrame):
        pass

    def interpret(self):
        pass
