fList = []
sList = []
sum1=0
sum2=0
len1 = int(input("How many numbers do you want to add in first list?"))
for i in range(0,len1):
    inp = int(input("Enter the value for element"))
    fList.append(inp)
len2 = int(input("How many numbers do you want to add in second list?"))
for i in range(0,len2):
    inp = int(input("Enter the value for element"))
    sList.append(inp)
if(len(fList) == len(sList)):
    print("Two lists are of same length")
else:
    print("Lists have different length")
for num in fList:
    sum1 += num
for num in sList:
    sum2 += num
if sum1==sum2:
    print("The sum of values of elements in both lists are equal")
else:
    print("Sum of values of both list's elements are different")
for num in fList:
    if num in sList:
        print(num," found in both lists\n")
