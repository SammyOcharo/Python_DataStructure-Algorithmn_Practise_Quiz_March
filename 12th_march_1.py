"""
Write a function for checking the speed of drivers. This function should have one parameter: speed.
If speed is less than 70, it should print “Ok”.
Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit point and print 
the total number of demerit points. For example, if the speed is 80, it should print: “Points: 2”.
If the driver gets more than 12 points, the function should print: “License suspended”
"""

def SpeedChecker(speed):

    if speed <= 70:
        print("Your speed is ok")
    
    else:
        if speed > 70:
            excessivespeed = speed - 70
            demerit = excessivespeed /5

            print("Points: ", round(demerit))
            if demerit >= 12.0 :
                print("License suspended")

if __name__ == '__main__':

    speed = int(input("Enter the speed: "))

    SpeedChecker(speed)