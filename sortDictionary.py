dict = dict()
n = int(input("How many items do you want to enter to the array?"))
for i in range(n):
    key = input("Enter the key")
    val = input("Enter value")
    dict[key] = val
print(dict)
print("Sorted [ascending]: ", sorted(dict.values()))
print("Sorted [descending]: ", sorted(dict.values(),reverse=True))