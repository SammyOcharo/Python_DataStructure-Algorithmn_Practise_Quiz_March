"""
Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
Note here exp is a non-negative integer, and the base is an integer.

Expected output

Case 1:

base = 2
exponent = 5

2 raises to the power of 5: 32 i.e. (2 *2 * 2 *2 *2 = 32)

"""

def Power(base, exponent):
    for i in range(1, exponent, 1):
        answer = base**exponent

    print("The answer is: ", answer)


if __name__ == '__main__':

    base = input("Enter base number: ")
    exponent = input("Enter exponent number: ")

    base = int (base)
    exponent = int(exponent)

    Power(base, exponent)