n=int(input("Enter the value of n:"))
rev=0

while n>0:
    temp=n%10
    rev=rev *10 +temp
    n//=10
print(rev)