def factorial(num):
    x= 1
    for i in range(1,num+1):
        x*=i
    return x
number = int(input("Enter a value to find factorial : "))
print("Factorial of {} is {}".format(number,factorial(number)))
