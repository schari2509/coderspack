#Triangle

a = input("Enter first side : ")
b = input("Enter second side : ")
c = input("Enter third side : ")

if a == b == c:
    print("Equilateral Triangle")
elif a == b or b == c or a == c:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")
