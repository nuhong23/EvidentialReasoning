
from parseDataToClass import *
from frame import *

def main():

    parse = ParseDataToClass()
    parse.openInputFile()

    print (parse.frames)
    print(parse.CR)

    frames = Frame(parse.frames)










if __name__ == "__main__":
    print("Entered main function")
    main()
else:
    print("Did not enter main function.")

