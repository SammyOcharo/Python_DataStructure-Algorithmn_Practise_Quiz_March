"""
Write a program to take number of days as input and convert and display it in years, months, weeks, and days 
(example: 452 days equals 1 year, 2 months, 3 weeks and 6 days ) Assume 365 days in a year and 30 days in a month
"""
def dayscalculator(days):
    year = 0
    month = 0

    if days == 0:
        print("Days entered is zero")
    else:
        while days >= 365:
            year = year + 1
            days = days - 365
    if days >= 30:
        while days >= 30:
            month = month + 1
            days = days - 30
    else:
        if days <= 30:
            days= days

    print ( f" The given days result to {year} year(s) {month} month(s) {days} day(s)" )


if __name__ == '__main__':

    days = input("Input the number of days: ")

    days = int(days)

    dayscalculator(days)