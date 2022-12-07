def fibonacci(n):
    first = 0
    second =1
    print(first)
    print(second)
    for i in range(n-2):
        third = first+second
        print(third)
        first = second
        second = third
fibonacci(int(input("Enter a number")))