# Author Tami Hong Le
# 3/7/2015
class ParseDataToClass:

    def __init__(self):
        pass

    def openInputFile(self):

        #open file, if path does not exist, print error message
        try:
            dir_path = input("Enter the path to the Input.txt file:   ")
            inFile = open(dir_path, 'r')

            str = ParseDataToClass()

            #parse the file by keywords: Question = Q, frame = B, and compatibility relations = CR
            for line in inFile:

                #send strings to methods by keyword
                if line.startswith('Q'):
                    str.parseDataToQuestionFrame(line)
                    print (line, end = '')
                elif line.startswith('B'):
                    str.parseDataToFrame(line)
                    print (line, end = '')
                elif line.startswith("CR"):
                    str.parseDataToCR(str)
                    print (line, end = '')
                else:
                    print ("Recheck your Input.txt file for consistency.\n")
                    print ("Question should use the abbreviation 'Q:' ")
                    print ("Frames should use the abbreviation 'B#:' where # is the sequential number starting from 1")
                    print ("Compatibility relations should use the abbreviation 'CR#:' where # is the sequential number starting from 1\n")
                    print ("The error exist in the line --->     " + line, end = '')
                    inFile.close()
                    break
            inFile.close()

        #throw an exception and reopen the openInputFile method again
        except FileNotFoundError:
            print("The directory path to Input.txt file is not valid.\n")
            reopen = ParseDataToClass()
            reopen.openInputFile()
        else:
            inFile.close()

    #creates a dictionary for the question frame with two arrays
    def parseDataToQuestionFrame(self, str):

        splitter = str.split(':',3)
        quest = [splitter[1], splitter[2]]
        answers = [splitter[3:len(splitter)]]

        questionFrame = {splitter[0]:[quest,answers]}

        return questionFrame


    def parseDataToFrame(self, str):

        print ("Entered FRAME")

        splitter = str.split(':')

    def parseDataToCR(self,str):
        print ("Entered CR")


'''
    if __name__ == "__main__":
        openInputFile()
        print("ParseDataToClass executed from within")
    else:
        print("ParseDataToClass imported into another module")

'''