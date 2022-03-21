"""
list1 = [100, 200, 300, 400, 500]
Expected output:

[500, 400, 300, 200, 100]

"""

def sortingList(list1):

    list1.reverse()

    print(list1)

if __name__ == '__main__':

    list1 = [100, 200, 300, 400, 500]

    sortingList(list1)