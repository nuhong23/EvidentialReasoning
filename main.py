
from parseDataToClass import *
from frame import *
from  CompatibilityRelations import *

def main():

    parse = ParseDataToClass()
    parse.openInputFile()

    print (parse.frames)
    print(parse.CR)

    #frames = Frame(parse.frames)
    #frames.organize_propositions(frames)

    #cr = CR(frames.crossProductFrames, parse.questionFramestion)










if __name__ == "__main__":
    print("Entered main function")
    main()
else:
    print("Did not enter main function.")

