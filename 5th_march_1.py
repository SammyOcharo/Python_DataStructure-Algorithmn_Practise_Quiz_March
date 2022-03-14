"""
Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.

A recursive function is a function that calls itself, again and again.
"""

def addition(num):
    if num:

        return num + addition(num-1)
    else:
        return 0

if __name__ == '__main__':

    res = addition(10)
    print(res)