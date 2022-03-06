"""
Write a Python program to accept a filename from the user and print the extension of that
"""

if __name__ == '__main__':

    file = input("Enter file to check extension: ")

    file = file.split(".")

    file_extension = file[-1]

    print("the extension type of the file is: ", file_extension)