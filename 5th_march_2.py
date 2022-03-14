"""
Generate a Python list of all the even numbers between 4 to 30

"""

def evenNumbers():
    listnumbers=[]

    for i in range(4, 30):
        if i % 2 ==0:
            listnumbers.append(i)

    print (listnumbers)


if __name__ == '__main__':

    evenNumbers()