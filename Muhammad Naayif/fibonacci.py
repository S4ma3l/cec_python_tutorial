def fibonacci(x):
    first = 0
    second = 1
    print(first)
    for i in range(x-1):
        print(second)
        third = first + second
        first = second
        second = third
limit = int(input("Enter how many numbers you want to print in the series."))
fibonacci(limit)