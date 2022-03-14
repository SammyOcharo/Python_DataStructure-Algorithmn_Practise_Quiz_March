"""
Create an outer function that will accept two parameters, a and b
Create an inner function inside an outer function that will calculate the addition of a and b
At last, an outer function will add 5 into addition and return it
"""

def function1(num1, num2):


    def function2(num1, num2):
        sum = num1+num2

        return sum

    add = function2(num1, num2)

    print ( add + 5 )


if __name__ == '__main__':

    num1 = input("Enter 1st number: ")
    num2 = input("Enter 2nd number: ")

    num1 = int(num1)
    num2 = int(num2)

    function1(num1, num2)