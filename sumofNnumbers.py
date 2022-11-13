def sumOfNNumbers(num,sum):
    for r in range(num+1):sum+=r
    return sum
print(sumOfNNumbers(int(input("Enter a number")),0)*2)
