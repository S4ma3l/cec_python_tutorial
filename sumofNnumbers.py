def sumOfNNumbers(num):
    sum=0
    for r in range(num+1):
        sum+=r
    return sum
print(sumOfNNumbers(int(input("Enter a number")))*2)
