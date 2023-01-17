import sys
character= 'a'

print(character * 10)
number= 8
print (number * 18)   #performs multibilication
print(str(number) * 10)



def variable_repeat(text,nooftimes):
    value=text*nooftimes
    return value

if __name__ == '__main__':
    text=sys.argv[1]
    nooftimes=int(sys.argv[2])
    print(variable_repeat(text,nooftimes))