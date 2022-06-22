

for row in range(1,7):
    for col in range(7-row-1):
        print(" ",end="")
    for col in range(row+1):
        print("*",end=" ")
    print()