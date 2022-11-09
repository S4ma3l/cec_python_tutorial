#Prompt the user for a list of integers. For all values greater than 100, store ‘over’ instead.
len = int(input("How many numbers do you want to store?"))
inpValueList = []
for num in range(0,len):
    inpValue = int(input("Enter value"))
    if inpValue>100:
        inpValueList.append("OVER")
    else:
        inpValueList.append(inpValue)
print(inpValueList)
