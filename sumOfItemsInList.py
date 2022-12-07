def total(_list):
    sum=0
    for x in _list:
        sum +=x
    return sum
_list =[]
n = int(input("How many numbers do you want to insert to the list? "))
for i in range(n):
     _list.append(int(input("Enter the elements for the list")))
print(total(_list))
