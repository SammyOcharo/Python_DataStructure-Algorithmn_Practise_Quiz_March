"""
Write a Python program which 
accepts the user's first and last name and print them in reverse order with a space between them
"""

def names(first_name, second_name):

    Reversed_first_name = first_name[::-1]
    Reversed_second_name = second_name[::-1]

    print("The original name is:", first_name, "", second_name, "and the reversed name is:", Reversed_first_name, "", Reversed_second_name)




if __name__ =='__main__':

    first_name = input("Enter first name: ")
    second_name = input("Enter second name: ")

    names(first_name, second_name)