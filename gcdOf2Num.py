def gcd(x,y):
    if x ==0:
        return "GCD = {}".format(y)
    if y==0:
        return "GCD = {}".format(x)
    factorList1 =[]
    factorList2=[]
    for i in range(1,x+1):
        if x%i == 0:
            factorList1.append(i)
    for i in range(1,y + 1):    
        if y % i == 0:
            factorList2.append(i)
    i=-1
    for factor in factorList1:

        if factorList1[i] in factorList2:
            return "GCD = {}".format(factorList1[i])
            break
        i-=1

a = int(input("Enter the value of a"))
b = int(input("Enter the value of b"))
print(gcd(a,b))