firstNameList = []
len = int(input("How many names do you want to insert"))
for i in range(0,len):
    fname = input("Enter the first name you want to add to list")
    firstNameList.append(fname)
    count_a = 0
for names in firstNameList:
    count_a += names.count("a")
print(count_a)