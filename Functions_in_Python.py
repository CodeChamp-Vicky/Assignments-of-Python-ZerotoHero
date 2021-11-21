"""
Functions
Types of Functions

1. Built-in functions. E.g., print(), len(), help(), int(), min(), max(), range(), str(), float(), list()

2. User defined functions E.g., These are created by user to solve certain problems
definition of function

    def <function_name>():
               statement 1
               statement 2
               .
               .
               .
               statement n
calling of function

  function_name()
"""


# help() This functions helps us in our doubts regarding Python programming
#  i.e., syntax and helps in finding various types of errors

num = [10, 20, 30, 41, 56, 11, 22]
print("Type of the variable num is", type(num))
print("Lowest Number in the List is ", min(num))
print("Highest Number in the List is ", max(num))
print("Length of the List is ", len(num))


# Function definition
def intro():
    print("\nHi ! This function is defined by me")


intro()  # Function calling


def add():
    print("Enter First Number :")
    a = int(input())
    print("Enter Second Number :")
    b = int(input())
    c = a+b
    print("Addition of {} and {} is ".format(a, b), c)


add()


def concat():
    print("\nEnter first string :")
    first = input()
    print("\nEnter second string :")
    second = input()
    out = first + " " + second
    print("\nConcatenated String :", out)


concat()


def multiply():
    print("Enter first number :")
    num1 = int(input())
    print("Enter second number :")
    num2 = int(input())
    num3 = num1 * num2
    print("Multiplication of {} and {} is ".format(num1, num2), num3)


multiply()


def circle_area():
    print("Enter the radius of circle :")
    r = float(input())
    pi = 3.14
    area = pi * (r ** 2)
    print("Area of your circle with radius {} is".format(r), area)


circle_area()


def rect_area():
    print("Enter length of the rectangle :")
    length = float(input())
    print("Enter breadth of the rectangle :")
    breadth = float(input())
    area1 = length * breadth
    print("Area of rectangle with length {} and breadth {} is ".format(length, breadth), area1)


rect_area()


def subtract():
    x = int(input("Enter first number :"))
    y = int(input("Enter second number :"))
    diff = x - y
    print("Difference between {} and {} is ".format(x, y), diff)


subtract()
