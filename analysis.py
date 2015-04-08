

class Analysis:

    translatedFrame = {}

    def __init__(self):
        pass

    def discount(self, mass):
        alpha = raw_input("What is the alpha number for adjustment? ")
        alpha = float(alpha)

        try:
            self.discounted = float(alpha) * float(mass)
            return self.discounted
        except TypeError:
            print("Error")

    def translate(self,frame1,relations1,frame2, relations2):
        print("printing in translating\n")
        splitter1 = relations1.split(',')
        splitter2 = relations2.split(',')

        product = []

        for i in splitter1:
            for j in splitter2:
                string = i + ',' + j
                product.append(string)

        translatedFrame = {(frame1[0] + 'x' + frame2[0]): product}
        print(translatedFrame)

        return translatedFrame

        #if frame1[1].upper() == 'YES':
            #discount(frame1[2],)




        print(frame1)
        print(relations1)
        print(frame2)
        print(relations2)
        #splitter = relations1.split(',')
        #print(splitter)



    # Dempster's combination rule
    def fuse(self,translatedFrame):
        pass

    def interpret(self):
        pass
