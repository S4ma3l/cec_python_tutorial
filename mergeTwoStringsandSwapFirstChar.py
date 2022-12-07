str1 = input("Enter the first string")
str2 = input("Enter the second string")
_str1 = str2[0] + str1[1:]
str2 = str1[0] + str2[1:]
newString = _str1 + " " + str2
print("Modified string : ", newString)

