"""
Write a function called show_stars(rows). If rows is 5, it should print the following:
*
**
***
****
*****
"""

def show_stars():

    for i in range(6):
        print("*"*i, end="")
        print("\n")

show_stars()