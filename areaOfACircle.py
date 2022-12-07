def findAreaOfCircle(r):
    area = 3.14 * r**2
    return area
r = int(input("Enter the radius of the circle"))
print("Area of the circle = ", findAreaOfCircle(r))