"""
Name: Jessica Andrews
sales_force.py

Problem: encapsulates data for a sales person
I certify that this program is entirely my own work
"""
from sales_person import SalesPerson
class SalesForce:
    def __init__(self):
        sales_people = []
        self.sales_people = sales_people


    def add_data(self,filename):
        open_file = open(filename,'r')
        lines = open_file.readline()


    def quota_report(self,quota):
        salesPeople = []
        open_file = open("test_hw10_data_b02fce0e",'r')
        lines = open_file.readline()
        seperate = lines.split(", ")
        id = int(seperate[0])
        name = seperate[1]
        person = SalesPerson(id, name)
        get_sales = seperate[2]
        indiv_sales = get_sales.split(" ")
        for sale in range(len(indiv_sales)):
            enter_sales = person.enter_sale(eval(indiv_sales[sale]))
        total_sales = person.total_sales()
        met_quota = person.met_quota(quota)
        salesPeople.append(id)
        salesPeople.append(name)
        salesPeople.append(total_sales)
        salesPeople.append(met_quota)
        return salesPeople
