vowels=["a","e","i","o","u"]

word = input("Enter a word")
vowelList = []
for alphabet in word:
    if alphabet in vowels:
        vowelList.append(alphabet)
print(vowelList)

