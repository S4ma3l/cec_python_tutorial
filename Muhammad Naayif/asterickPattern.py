def createPattern(limit):
    for i in range(1,limit+1):
        for x in range(i):
            print("*",end=" ")
        print("\n")
    for i in range(limit-1,0,-1):
        for x in range(i):
            print("*",end=" ")
        print("\n")
len = int(input("How many lines do you want to add to the pattern"))
createPattern(len)


