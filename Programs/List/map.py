def add(n):
    return n*n
list1=[2,3,4,5]# tuple=(3,4,5,6)
result=map(add,list1)# result =map(add,tuple)
print(list(result))