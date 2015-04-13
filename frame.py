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


    #to get the cross product frames after discount and translating operations
    def get_crossProductFrames(self, FOD1, FOD2):

        cross = Analysis()
        relations1 = []
        relations2 = []

        splitter1 = FOD1.split(':')
        splitter2 = FOD2.split(':')

        alpha1 = splitter1[3]
        alpha2 = splitter2[3].strip()
        mass1 = splitter1[4].strip()
        mass2 = splitter2[4].strip()

        discountOption1 = splitter1[2].upper().strip()
        discountOption2 = splitter2[2].upper().strip()

        #iterates through the FOD list and check for discounting operation
        for elements in FOD1,FOD2:
            #accounts for the discount operation before crossing the frames
            if discountOption1 == 'YES':
                discounts1 = Analysis()
                discounts1.discount(alpha1, mass1)
                splitter1[4] = discounts1.discounted
                splitter1[3] = 0
                splitter1[2] = "NO"
                print(discounts1.discounted)
                print('\n')
                break

            elif discountOption2 == 'YES':
                discounts2 = Analysis()
                discounts2.discount(alpha2, mass2)
                splitter2[4] = discounts2.discounted
                splitter2[3] = 0
                splitter2[2] = "NO"
                print(discounts2.discounted)
                print('\n')
                break

        length_ofFrameInfo1 = len(splitter1) - 1
        length_ofFrameInfo2 = len(splitter2) - 1
        print("length of frame information is : " + str(length_ofFrameInfo1))

        frameInfo1 = splitter1[1: length_ofFrameInfo1]
        relations1.append(splitter1[length_ofFrameInfo1].split(','))
        relation1 = splitter1[length_ofFrameInfo1].split(',')

        frameInfo2 = splitter2[1: length_ofFrameInfo2]
        relations2.append(splitter2[length_ofFrameInfo2].split(','))
        relation2 = splitter2[length_ofFrameInfo2].split(',')

        string =''

        for i in relation1:
            for j in relation2:
                string = string + i + j + ','

        insertFrame = "FOD:" + frameInfo1[0] + 'x' + frameInfo2[0] + ': NO:' + '0:' + string

        print(frameInfo1)
        print(frameInfo2)

        cross.translate(frameInfo1, relations1, frameInfo2, relations2)

        return cross.translate

