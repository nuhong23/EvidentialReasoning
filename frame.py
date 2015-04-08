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
    def crossProductFrames(self, FOD, framesInfo):
        print("\nEntering the cross product frame: \n")
        print(FOD)
        i = 0

        #iterates through the FOD list and continues to organize it in preparation for
        #frame translating
        for elements in FOD:
            splitter = elements.split(":")
            alpha = splitter[3].strip()
            float(alpha)
            mass = splitter[4].strip()
            float(mass)

            discountOption = splitter[2].upper().strip()

            #accounts for the discount operation before crossing the frames
            if discountOption == 'YES':
                print("Entering discount")
                discounts = Analysis()
                discounts.discount(alpha, mass)
                splitter[3] = discounts.discounted
                print(discounts.discounted)

            self.frameName.append(splitter[1:6])
            self.relations.append(splitter[6])

            name = splitter[1]
            self.frames[name] = self.relations[i]
            i = i + 1

        print(self.frameName)
        print(self.frames)

        cross = Analysis()
        x = 0

        #keeps invoking the translate operation until it is out of range
        while range(0,len(self.frameName)+ 2):
            try:
                if len(self.frameName) != 0:
                    cross.translate(self.frameName[x],self.relations[x],self.frameName[x + 1], self.relations[x + 1])

                    self.frameName.remove(self.frameName[x])
                    self.frameName.remove(self.frameName[x])
                    self.frameName.insert(x, cross.newFrame)

                    self.relations.remove(self.relations[x])
                    self.relations.remove(self.relations[x])
                    self.relations.insert(x, cross.newRelations)

                    newFrame = cross.newFrame
                    self.frames[newFrame] = cross.newRelations

            except (IndexError,TypeError):
                continue

        #check to see if any of the frames have matching information
        for x in self.frameInfo:
            print("frame info")
            print(x)

        print(self.frames)
        return self.frames

