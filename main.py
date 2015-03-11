
from parseDataToClass import *
from frame import *
from  compatibilityRelations import *

def main():

    parse = ParseDataToClass()
    parse.openInputFile()

    print (parse.frames)
    print(parse.CR)
    print(parse.questionFrame)
    print(parse.relations)
    print('\n')


    frames = Frames()
    frames.organize_frames(parse.frames, parse.relations)
    print(frames.frameInfo)
    print(frames.propositions)



    #cr = CR(frames.crossProductFrames, parse.questionFramestion)










if __name__ == "__main__":
    print("Entered main function")
    main()
else:
    print("Did not enter main function.")

