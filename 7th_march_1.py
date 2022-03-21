"""
Write a program that takes in price of maize in a week as a list and computes the maximum profit on the specific days 
and outputs the days. Its should also output an error when the last day of the week has a lower price than the 1st day

"""

def PriceOfMaize(PriceAcrossTheWeek):

    if PriceAcrossTheWeek[-1] < PriceAcrossTheWeek[0]:
        print("You cannot sell of a lower amount as the one you purchased")
    else:
        maximum = 0
        for i in range(len(PriceAcrossTheWeek)-1):
            maximum1 = PriceAcrossTheWeek[i+1] - PriceAcrossTheWeek[i] 
            if maximum1 > maximum:
                maximum = maximum1

        print (f"The maximum profit is : { maximum}")


if __name__ == '__main__':


    PriceAcrossTheWeek = [100,150,140,650,120,560,506]

    PriceOfMaize(PriceAcrossTheWeek)