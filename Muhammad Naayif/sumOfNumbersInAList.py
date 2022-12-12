# program to find sum of all numbers in a list.
limit = int(input("Enter the number of elements to insert into the list: "))
numList = []
for i in range(limit):
    val = int(input("Enter value: "))
    numList.append(val)
sumOfList = 0
for num in numList:
    sumOfList+=num
print("Sum of elements of list is {}".format(sumOfList))