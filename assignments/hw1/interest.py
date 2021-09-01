"""
Name: Jessica Andrews
interest.py

Problem: A program that computes the monthly interest charge on a credit card account
I certify that this assignment is entirely my own work.
"""
def monthly_intrest():
    annual = eval(input("What is your annual interest rate?:"))
    days = eval(input("What is the number of days in your billing cycle?:"))
    previous_balance = eval(input("What is your previous net balance?:"))
    payment_amount = eval(input("What is your payment amount?:"))
    day_of_billing_cycle = eval(input("What is the day of the billing cycle in which the payment was made?:"))
    monthly_rate = annual/12
    calc1 = previous_balance * days
    days_before_end = days - day_of_billing_cycle
    calc2 = payment_amount * days_before_end
    calc3 = calc1 - calc2
    average_daily_balance = calc3 / days
    monthly = average_daily_balance * monthly_rate/100
    print("your monthly intrest rate is:", monthly)
monthly_intrest()



