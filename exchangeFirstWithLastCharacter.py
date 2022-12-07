def replaceFirstWithLast(str):
    modifiedString = str[-1]+str[1:-1]+str[0]
    return modifiedString
result = replaceFirstWithLast(input("Enter the string you want to modify"))
print("Modified String = ", result)
