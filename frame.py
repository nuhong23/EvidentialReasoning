from analysis import *

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

        for elements in FOD:
            splitter = elements.split(":")
            self.frameName.append(splitter[1:4])
            self.relations.append(splitter[4])
            countFOD = len(FOD)

        cross = Analysis()
        x = 0

        while x < countFOD:
            try:
                cross.translate(self.frameName[x],self.relations[x],self.frameName[x+1], self.relations[x+1])
                x = x + 1
            except:
                break






