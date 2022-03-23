"""
Write a function that returns the maximum of two numbers.
"""

def maxvalue(int1, int2):

    if int1 > int2:

        print("The maximum value is: ", int1)

    else:
         print("The maximum value is: ", int2)

if __name__ == '__main__':

    int1 = input("Enter first number: ")
    int2 = input("Enter second number: ")

    int1 = int(int1)
    int2 = int(int2)

    maxvalue(int1, int2)