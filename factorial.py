def fact(x):
    fact =1
    for i in range(1,x+1):
        fact = fact * i
        i+=1
    return fact
print(fact(int(input("Enter a number"))))