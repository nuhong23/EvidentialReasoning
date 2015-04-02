
from parseDataToClass import *
from frame import *
from compatibilityRelations import *

def main():

    parse = ParseDataToClass()
    parse.openInputFile()
    print("Parsed Information for frames, CR, and Question\n")
    print (parse.frames)
    print(parse.CR)
    print(parse.questionFrame)
    print('\n')


    frames = Frames()
    frames.organize_frames(parse.frames)
    print("Frame information and its propositions organized into an array\n")
    print(frames.frameInfo)
    print(frames.propositions)
    print('\n')

    relations = CompatibilityRelations()
    relations.organize_relations(parse.CR)
    print("Compatibility relations\n")
    print(relations.compatibilityInfo)
    print(relations.relatedTo)

    for elements in frames.frameInfo:
            try:
                discountPrompt = input("Is discounting needed for: " + elements[0] + "?\n");

                if discountPrompt.upper() == "YES":
                    alpha = input("Enter the alpha value between 0 and 1")
                    print(alpha)

            except IOError:
                print("The answer must be 'YES' or 'NO'")





if __name__ == "__main__":
    main()


