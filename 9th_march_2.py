"""
Given a two Python list. Write a program to iterate both lists simultaneously and 
display items from list1 in original order and items from list2 in reverse order.

Given

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

Expected output:

10 400
20 300
30 200
40 100

"""

def listing(list1, list2):

    for x, y in zip(list1, list2[::-1]):
        print(x, y)

    return

if __name__ == '__main__':

    list1 = [10, 20, 30, 40]
    list2 = [100, 200, 300, 400]

    listing(list1, list2)
