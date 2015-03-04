
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

        dir_path = input("Enter the path to the Input.txt file: ")
        file = open(dir_path + '/Input.txt', 'r')
        print(file.readline())

        for line in file:

            print(line, end = '')
        return


dog = ParseDataToClass()
dog.openInputFile()


'''
    if __name__ == "__main__":
        openInputFile()
        print("ParseDataToClass executed from within")
    else:
        print("ParseDataToClass imported into another module")

'''