"""
Write a Python program that accept a list of integers and check the length and the fifth element. 
Return true if the length of the list is 8 and fifth element occurs thrice in the said list. 
Input:
[19, 19, 15, 5, 5, 5, 1, 2]
Output:
True
"""




def list_integer(Input):
    total = 0
    if len(Input) == 8:
        for i in range(len(Input)):
            if Input[i] == 5:
                total += 1
        if total >= 3:
            print("True")
        else:
            print("False") 

if __name__ == '__main__':

    Input = [19, 19, 15, 5, 5, 5, 1, 2]

    list_integer(Input)