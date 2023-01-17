import sys

def printtext(name):
    print("this is my second python program using sys",name, sep=" - ")
    print("print the second line" + name , end="." )
    
    
    # predefined main function
if __name__ == '__main__':
    #printtext("OMR")
    printtext(sys.argv[1]) # 'sys.argv[]' used to get first command line arguments
    