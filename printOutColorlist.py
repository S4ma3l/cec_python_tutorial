colorList1 = input("Enter color names for list 1 seperated by a comma").split(",")
colorList2 = input("Enter color names for list 2 seperated by a comma").split(",")
for color in colorList1:
    if color not in colorList2:
        print(color)
