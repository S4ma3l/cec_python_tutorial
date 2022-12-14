def pyramid(r):
    for i in range(1,r+1):
        for x in range(i,i*i+1,i):
            print(x,end=" ")
        print("\n")



n = int(input("Enter a number: "))
pyramid(n)

