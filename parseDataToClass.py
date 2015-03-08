
#s = 'This is a string of words'
#s.split()

#str.startswith (str, beg=0, end = len(s)); >> True or False

#list as arrays
# use list = []
# del list1[2];

class ParseDataToClass:


    def __init__(self):
        pass

    def openInputFile(self):

        #open file, if path does not exist, print error message
        try:
            dir_path = input("Enter the path to the Input.txt file: ")
            file = open(dir_path + '/Input.txt', 'r')
            print(file.readline())

            #parse the file for keywords of frame and CR
            for line in file:
                if line.read(1) =="B":
                    print (line.read(1), end = '')

        #throw an exception and reopen the openInputFile method again
        except FileNotFoundError:
            print("The Input.txt file you have entered is not valid. Make sure the text file is named ""Input.txt""")
            reopen = ParseDataToClass()
            reopen.openInputFile()
        else:
            file.close()



    def parseDataToFrame(self):
        pass

    def parseDataToCR(self):
        pass


'''
    if __name__ == "__main__":
        openInputFile()
        print("ParseDataToClass executed from within")
    else:
        print("ParseDataToClass imported into another module")

'''