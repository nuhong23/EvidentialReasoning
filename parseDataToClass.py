# Author Tami Hong Le
# 3/7/2015
class ParseDataToClass:


    def __init__(self):
        pass

    def openInputFile(self):

        #open file, if path does not exist, print error message
        try:
            count = 0
            frames = []
            CR = []

            dir_path = input("Enter the path to the Input.txt file:   ")
            inFile = open(dir_path, 'r')

            str = ParseDataToClass()

            #parse the file by keywords: Question = Q, frame = B, and compatibility relations = CR
            for line in inFile:

                #send strings to methods by keyword
                if line.startswith('Q'):
                    str.parseDataToQuestionFrame(line)

                elif line.startswith('B'):
                    str.parseDataToFrame(frames, line)

                elif line.startswith("CR"):
                    str.parseDataToCR(CR, line)
                    #print (line, end = '')
                else:
                    print ("Recheck your Input.txt file for consistency.\n")
                    print ("Question should use the abbreviation 'Q:' ")
                    print ("Frames should use the abbreviation 'B#:' where # is the sequential number starting from 1")
                    print ("Compatibility relations should use the abbreviation 'CR#:' where # is the sequential number starting from 1\n")
                    print ("The error exist in line --->     " + line, end = '')
                    inFile.close()
                    break
            print(frames)
            print(CR)
            inFile.close()

        #throw an exception and reopen the openInputFile method again
        except FileNotFoundError:
            print("The directory path to Input.txt file is not valid.\n")
            reopen = ParseDataToClass()
            reopen.openInputFile()
        else:
            inFile.close()

    # packages two arrays into a dictionary
    def parseDataToQuestionFrame(self, str):

        splitter = str.split(':',3)
        quest = [splitter[1], splitter[2]]
        answers = [splitter[3:len(splitter)]]

        questionFrame = {splitter[0]:[quest,answers]}

        return questionFrame


    def parseDataToFrame(self, frames, str):
        frames.append(str.rstrip('\n'))
        return frames

    def parseDataToCR(self, CR, str):
        CR.append(str)
        return CR





'''
    if __name__ == "__main__":
        openInputFile()
        print("ParseDataToClass executed from within")
    else:
        print("ParseDataToClass imported into another module")

'''