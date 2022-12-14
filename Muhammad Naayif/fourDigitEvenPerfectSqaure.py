#Generate a list of four digit numbers in a given range with all their digits even and the
#number is a perfect square.

import math


def isPerfectSquare(x):
	if(x >= 0):
		root = int(math.sqrt(x))
		return ((root*root) == x)
	return False

excludeList = [1,3,5,7,9]
evenList = [2,4,6,8,0]
def allEven(num):
    while(num>0):
        if(num%10 in excludeList):
            return False
        else:
            num = num//10
    return True


def numberCombinations(x,y):
    for i in range(x,y+1):
        if (i//1000) not in excludeList:
            root = int(math.sqrt(i))
            if(isPerfectSquare(i)):
                if allEven(i):
                    print("{}, and {}".format(i,int(math.sqrt(i))))





def takeInput():
    s_range = int(input("Enter the starting range: "))
    f_range = int(input("Enter the stopping range: "))
    if s_range>= 1000 and f_range>=1000:
        numberCombinations(s_range,f_range)
    else:
        takeInput()

takeInput()