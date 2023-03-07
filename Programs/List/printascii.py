for i in range(65,91):
   print(chr(i))

a=65
for i in range(0,3):
   for j in range(0,i+1):
      print(chr(a),end=" ")
   print("\n")
   a=a+1