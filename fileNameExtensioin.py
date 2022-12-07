def filenameExtension(s):
    return s[s.index(".")+1:]
extension = filenameExtension(input("Enter a filename with extension"))
print("File extension is ", extension)