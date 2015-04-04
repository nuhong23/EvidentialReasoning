
from parseDataToClass import *
from frame import *
from compatibilityRelation import *
from analysis import *

def main():

    parse = ParseDataToClass()
    parse.openInputFile()
    print("Parsed Information for frames, CR, Question AND FOD \n")
    print(parse.questionFrame)
    print (parse.frames)
    print(parse.CR)
    print(parse.FOD)
    print('\n')


    frames = Frames()
    frames.organize_frames(parse.frames)
    frames.crossProductFrames(parse.FOD)
    print("\nFrame information and its propositions organized into an array\n")
    print(frames.frameInfo)
    print(frames.propositions)
    print('\n')

    relations = CompatibilityRelations()
    relations.organize_relations(parse.CR)
    print("Compatibility relations\n")
    print(relations.compatibilityInfo)
    print(relations.relatedTo)






if __name__ == "__main__":
    main()


