def armstrong(num):
    temp = num
    sum =0
    order = len(str(temp))
    while(temp>0):
        lastno = temp % 10
        sum += lastno ** order
        temp = temp//10
    if sum == num:
        print(num," is an armstrong number")
    else:
        print(num, "is not an armstrong number")

armno = int(input("Enter a number to check for armstrong number"))
armstrong(armno)