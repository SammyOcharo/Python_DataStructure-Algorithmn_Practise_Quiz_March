"""
Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter). 
For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.
"""

def sumMultiples(StartingPoint, limit):
    sum = 0
    for i in range(StartingPoint, limit, 1):
        if i % 3 == 0 and i % 5 == 0:
            sum = sum+i
    print("The sum is:", sum)


if __name__ == '__main__':

    StartingPoint = int(input("Enter the starting point: "))
    limit = int(input("Enter the ending point: "))

    sumMultiples(StartingPoint, limit)