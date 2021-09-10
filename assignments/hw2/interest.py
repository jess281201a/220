"""
Name: Jessica Andrews
interest.py

Problem: A program that computes the monthly interest charge on a credit card account
I certify that this assignment is entirely my own work.
"""


def main():

    # these are input comments for variables
    rate = eval(input('What is your annual interest rate?:'))
    days = eval(input('What is the number of days in your billing cycle?:'))
    previous_balance = eval(input('What is your previous net balance?:'))
    payment = eval(input('What is your payment amount?:'))
    payment_day = eval(input('What is the day of the billing'
                             ' cycle in which the payment was made?:'))
    # formula's are used here
    monthly_rate = rate/12
    calc1 = previous_balance * days
    days_before_end = days - payment_day
    calc2 = payment * days_before_end
    calc3 = calc1 - calc2
    average_daily_balance = calc3 / days
    monthly = round(average_daily_balance * monthly_rate/100, 2)
    print(monthly)


if __name__ == '__main__':
    main()
