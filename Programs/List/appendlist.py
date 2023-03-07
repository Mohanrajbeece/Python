a=int(input("Enter the value of n:"))
sum=[]

while a>0:
    temp=a%10
    sum.append(temp)
    a=a//10
print(sum)