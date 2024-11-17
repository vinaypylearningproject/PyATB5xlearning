#Write a program that classifies a triangle based on its side lengths.
#Given three input values representing the lengths of the sides,
#determine if the triangle is equilateral (all sides are equal), isosceles
#(exactly two sides are equal), or scalene (no sides are equal).
#Use an if-else statement to classify the triangle.012

a=int(input("enter the value of a\n"))
b=int(input("enter the value of b\n"))
c=int(input("enter the value of c\n"))
if a==b and a==c:
    print("-----------")
    print("equilateral Triangle")
elif a==b or b==c or c==a:
    print("-----------")
    print("isosceles Triangle")
else:
    print("-----------")
    print("scalene Triangle")
