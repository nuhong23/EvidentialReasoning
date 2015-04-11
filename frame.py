from analysis import *


class Frames:

    mainPropositions = []
    mainFrame = []


    def __init__(self):
        pass

    #orgaizes the frames into lists
    def organize_frames(self,frames):
        for elements in frames:
            splitter = elements.split(":")
            self.mainFrame.append(splitter[1:4])
            self.mainPropositions.append(splitter[5].split('/'))
        return self.mainFrame, self.mainPropositions


    def get_crossProductFrames(self, FOD1, FOD2):

        cross = Analysis()
        relations1 = []
        relations2 = []

        splitter1 = FOD1.split(':')
        splitter2 = FOD2.split(':')

        frameInfo1 = splitter1[1:7]
        relations1.append(splitter1[7].split(','))
        relation1 = splitter1[7].split(',')
        print(relations1)

        frameInfo2 = splitter2[1:7]
        relations2.append(splitter2[7].split(','))
        relation2 = splitter2[7].split(',')
        print(relations2)

                #iterates through the FOD list and continues to organize it in preparation for
        #frame translating
        for elements in FOD1,FOD2:
            alpha = float(splitter1[3].strip())
            alpha = float(splitter2[3].strip())
            mass = float(splitter1[4].strip())
            mass = float(splitter2[4].strip())

            discountOption1 = splitter1[2].upper().strip()
            discountOption2 = splitter2[2].upper().strip()

            #accounts for the discount operation before crossing the frames
            if discountOption1 == 'YES':
                print("Entering discount")
                discounts = Analysis()
                discounts.discount(alpha, mass)
                splitter1[3] = discounts.discounted
                print(discounts.discounted)

            if discountOption2 == 'YES':
                print("Entering discount")
                discounts = Analysis()
                discounts.discount(alpha, mass)
                splitter2[3] = discounts.discounted
                print(discounts.discounted)

        cross.translate(frameInfo1, relations1, frameInfo2, relations2)

        #for i in relation1:
            #for j in relation2:
                #key = "FOD:" + frameInfo1[1] + 'x' + frameInfo2 + ':' + 'NO' + '0' + frameInfo1


        return cross.translate

