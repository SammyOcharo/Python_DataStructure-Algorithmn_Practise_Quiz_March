"""
Write a Python program to display the first and last colors from the following list. 
color_list = ["Red","Green","White" ,"Black"]
"""

def Color_list(color_list):

    first_color = color_list[0]
    last_color = color_list[-1]

    print("The first color is: ", first_color, "The last color is: ", last_color)


if __name__ == '__main__':

    color_list = ["Red","Green","White" ,"Black"]

    Color_list(color_list)

