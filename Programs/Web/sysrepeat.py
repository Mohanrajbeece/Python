import sys

def printtext(name):
    print("Hello" , name , sep="-")
    print("bye" , name)
    
if __name__ == '__main__':
     printtext(sys.argv[1])
     printtext(sys.argv[2])
     printtext(sys.argv[3])