"""
Given two lists, l1 and l2, write a program to create a third list l3 by picking an odd-index element from the list l1 and even index elements from the list l2.

Given:

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
Expected Output:

Element at odd-index positions from list one
[6, 12, 18]
Element at even-index positions from list two
[4, 12, 20, 28]

Printing Final third list
[6, 12, 18, 4, 12, 20, 28]

"""

def oddEvenAlign(L1, L2):
    L3 = []

    for i in range(len(L1)):
        if i % 2 == 1 :

            L3.append(L1[i])

    for i in range(len(L2)):
        if i % 2 == 0 :
            L3.append(L2[i])

    print(L3)

if __name__ == '__main__':

    L1 = [3, 6, 9, 12, 15, 18, 21]
    L2 = [4, 8, 12, 16, 20, 24, 28]

    oddEvenAlign(L1, L2)