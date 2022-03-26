"""
Write a Python program to find the indices of two numbers that sum to 0 in a given list of numbers. Go to the editor
Input:
[1, -4, 6, 7, 4]
Output:
[4, 1]
Input:
[1232, -20352, 12547, 12440, 741, 341, 525, 20352, 91, 20]
Output:
[1, 7]
"""

def sumofindeces(Input):

    for i in range(len(Input)):
        for j in range(len(Input)):

            if Input[i] + Input[j] == 0:

                print(f"The indices at {i} and {j} add upto 0")
            

    return
Input = [1, -4, 6, 7, 5, -7]
print("The original list is: ", Input)
print(sumofindeces(Input))


