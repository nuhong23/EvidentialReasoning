
from parseDataToClass import *
from frame import *
from compatibilityRelations import *

def main():

    parse = ParseDataToClass()
    parse.openInputFile()
    print("Parsed Information for frames, CR, and Question")
    print (parse.frames)
    print(parse.CR)
    print(parse.questionFrame)
    print('\n')


    frames = Frames()
    frames.organize_frames(parse.frames)
    print("Frame information and its propositions organized into an array")
    print(frames.frameInfo)
    print(frames.propositions)
    print('\n')

    relations = CompatibilityRelations()
    relations.organize_relations(parse.CR)
    print("Compatibility relations")
    print(relations.compatibilityInfo)
    print(relations.relatedTo)
    
    #for elements in
    #discountPrompt = raw_input("")






if __name__ == "__main__":
    main()


