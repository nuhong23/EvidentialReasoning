from analysis import *
from signal import signal, alarm, SIGALRM

# Author Tami Hong Le
# 3/7/2015
#
# organize_frames:  Organizes the frames information and propositions into another list
#
# loops over each index of the frames list, extract the frame information and
# propositions. Each elements are assigned in a new list called framesInfo and
# propositions.


class Frames:

    propositions = []
    frameInfo = []
    frameName = []
    relations = []
    frames = {}


    def __init__(self):
        pass



    #orgaizes the frames into lists
    def organize_frames(self,frames):

        for elements in frames:
            splitter = elements.split(":")

            self.frameInfo.append(splitter[1:4])
            self.propositions.append(splitter[5].split('/'))

        return self.frameInfo, self.propositions



    #crossing the frames to get a common cross product frame
    def crossProductFrames(self,FOD):
        print("\nEntering the cross product frame: \n")
        print(FOD)
        i = 0

        #iterates through the FOD list and continues to organize it in preparation for
        #frame translating
        for elements in FOD:
            splitter = elements.split(":")
            mass = splitter[3].strip()
            float(mass)
            discountOption = splitter[2].upper().strip()

            #accounts for the discount operation before crossing the frames
            if discountOption == 'YES':
                print("Entering discount")
                discounts = Analysis()
                discounts.discount(mass)
                splitter[3] = discounts.discounted


                print(discounts.discounted)

            self.frameName.append(splitter[1:4])
            self.relations.append(splitter[4])

            name = splitter[1]
            self.frames[name] = self.relations[i]
            i = i + 1

        countFOD = len(self.frames)
        print(countFOD)
        print(self.frameName)
        print(self.frames)

        cross = Analysis()
        x = 0

        while x < countFOD:
            try:
                cross.translate(self.frames)
                x = x + 2

            except:
                break







