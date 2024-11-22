#Increasing Triangle
row=int(input("Enter the number of rows: "))
for i in range(0,row):
    for j in range(0,i+1):
        print("*",end="")
    print("")
#Decreasing Triangle
row=int(input("Enter the number of rows: "))
for i in range(row,0,-1):
    for j in range(0,i):
        print("*",end="")
    print("")
#Hill pattern
row=int(input("Enter the number of rows: "))
for i in range(1,row+1):
    for j in range(row-i):
        print(" ",end=" ")
    for k in range((i*2)-1):
        print("*",end=" ")
    print("")
#Reverse Hill Pattern
row=int(input("Enter the number of rows"))
for p in range(row,0,-1):
    for q in range(row-p,0,-1):
        print(" ",end=" ")
    for r in range(2*p-1,0,-1):
        print("*",end=" ")
    print("")


