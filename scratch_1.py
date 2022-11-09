numlist = []
sqrList =[]
r = int(input("Enter numbers to calculate sqaure of"))
for num in range(0,r):
    inp = int(input("Enter a number"))
    numlist.append(inp)
for num in numlist:
    sqrList.append(num**2)
print(sqrList)