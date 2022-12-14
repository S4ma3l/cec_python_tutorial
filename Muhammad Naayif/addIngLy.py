def addIngOrLy(str):
    if(str[-3:] == "ing"):
        str= str + "ly"
    else:
        str = str + "ing"
    return str
word = input("Enter a word to modify")
modifiedString = addIngOrLy(word)
print("Modified string = ", modifiedString)
