def splitColorNames(str):
    c_list = str.split(",")
    return c_list
colors = input("Enter a series of color names seperated by comma")
colorList = splitColorNames(colors)
print("First color = ",colorList[0]," Last color = ",colorList[-1])

