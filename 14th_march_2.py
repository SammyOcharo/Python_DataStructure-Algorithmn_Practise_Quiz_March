"""
Write a Python program find a list of integers with exactly two occurrences of nineteen and 
at least three occurrences of five. 
Input:
[19, 19, 15, 5, 3, 5, 5, 2]
Output:
True

"""

def finder(Input):
    nineteenCount = 0
    fiveCount = 0

    for i in range(len(Input)):
        if Input[i] == 19:
            nineteenCount += 1
        if Input[i] == 5:
            fiveCount += 1
        
    if nineteenCount >= 2 and fiveCount >= 3:

        print("True")
    else: 
        print("False")

if __name__ == '__main__':

    Input = [19, 19, 15, 5, 3, 5, 5, 2]

    finder(Input)