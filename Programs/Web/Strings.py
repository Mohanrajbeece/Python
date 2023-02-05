#Printing just a integer
Number=10
print(Number)

#int+int perform additon
print(30+40)

#string+string perform concatenation with plus symbol
print("30"+'40')
#str+int or int+str produce type error
# print('10' + 10) # TypeError: can only concatenate str (not "int") to str

#adding integer to integer
print(Number+10)

#Printing string
name_1='python'
print(name_1)

#finding the length of string
name_2='mohan'
print(len(name_2))
print(type(name_2))
print(type(len(name_2)))

#concatenation of strings
result=name_1+name_2
print(result)

#adding integer to string/integer converted into string type
#output="name_1" + len(name_2) #TypeError: can only concatenate str (not "int") to str
result2=name_1+' '+str(len(name_2))
result1='name_1'+' '+str(len(name_2))
print(result1)
print(result2)

# adding integer to the string | string converted to integer type
num='27'
print(8+int(num))

#num1='abcd'
#print(8+int(num1)) #ValueError: invalid literal for int() with base 10: 'abcd'