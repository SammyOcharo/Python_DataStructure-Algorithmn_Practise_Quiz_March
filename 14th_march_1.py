"""
Write a function that prints all the prime numbers between 0 and limit where limit is a parameter.
"""

def primeNumbers(endingPoint):
    sum = 0
    for i in range(1, endingPoint, 1):
        
        if i / i == 1 and i/1 == i and i % 2 !=0 and i % 3 !=0 :

            sum = sum + i
    print(f"The sum of prime numbers from 0 to {endingPoint} is {sum}")

if __name__ == '__main__':

    endingPoint = int(input("Enter the ending value: "))

    primeNumbers(endingPoint)