a=[21,76,43,22]
min=a[0]
for i in range(1,len(a)):
    if min<a[i]:
     min=a[i]
print(min)


a=[45,67,89,75,43]
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i]<a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print(0)