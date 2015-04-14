
from parseDataToClass import *
from compatibilityRelation import *
from frame import *
from analysis import *

def main():

    parse = ParseDataToClass()
    parse.openInputFile()

    print("Parsed Information for frames, CR, Question, AND FOD \n")
    print(parse.questionFrame)
    print (parse.frames)
    print(parse.CR)
    print(parse.FOD)
    print('\n\n')

    countFOD = len(parse.FOD)
    frames = Frames()
    frames.organize_frames(parse.frames)
    print(frames.mainFrame)
    print(frames.mainPropositions)
    print(countFOD)

    newFrame = Analysis()

    while countFOD != 0:
        try:
            frames.get_crossProductFrames(parse.FOD[0], parse.FOD[1])
            parse.FOD.remove(parse.FOD[0])
            parse.FOD.remove(parse.FOD[0])
            #parse.FOD.insert(0, newFrame.insertFrame)

            #print("printing parse FOD from main")
            #print(parse.FOD)
            #print(countFOD)
        except IndexError:
            break

    print('\n\n')

'''
    relations = CompatibilityRelations()
    relations.organize_relations(parse.CR)
    print("Compatibility relations\n")
    print(relations.compatibilityInfo)
    print(relations.relatedTo)
'''





if __name__ == "__main__":
    main()


