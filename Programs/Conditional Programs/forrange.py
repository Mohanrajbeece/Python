
a=[2,4,6,8,10,12,14,16,18,20] 
for i in range(1,len(a),2):
    print(a[i]**a[i])
    
b=[1,16,8,2,5]
for c in range(0,len(b)):
    if b[c]%2==0:
        print(b[c]**2)