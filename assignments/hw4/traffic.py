"""
Name: Jessica Andrews
traffic.py

Problem: calculate the average of all the cars with the inputs put in by the user
I certify that this program is entirely my own work

"""


def main():

    # variables declared
    aver = 0
    all_cars = 0
    # inputs put in my user
    roads = eval(input("How many roads were surveyed?:"))

    # loops needed3
    for _ in range(0, roads):
        add = 0
        days = eval(input("How many days was the road surveyed?:"))
        for _ in range(0, days):
            cars = eval(input("How many cars traveled?:"))
            add = add + cars
            all_cars = all_cars + cars
            aver = add / days
        print("the roads average vehicles is:", round(aver, 2))
    aver_road = all_cars/roads
    print("Total number of vehicles traveled on all roads:", round(all_cars, 2))
    print("Average number of vehicles per road:", round(aver_road, 2))


if __name__ == '__main__':
    main()
