def changeOccurance(s):
    mod_string = s[1:].replace(s[0],"$")
    mod_string = s[0]+mod_string
    return mod_string
result = changeOccurance(input("Enter the string you want to modify"))
print("Modified string : ",result)
