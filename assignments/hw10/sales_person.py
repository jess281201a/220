"""
Name: Jessica Andrews
sales_person.py

Problem: encapsulates data for a sales person
I certify that this program is entirely my own work
"""
class SalesPerson:

    def __init__(self,employee_id,name):
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def get_id(self):
        employee_id = self.employee_id
        return int(employee_id)

    def set_name(self,name):
        self.name = name


    def get_name(self):
        return self.name

    def enter_sale(self,sale):
        self.sales.append(sale)

    def total_sales(self):
        total = 0
        for sale in self.sales:
            total += sale
        return total

    def get_sales(self):
        return self.sales

    def met_quota(self,quota):
        total = self.total_sales()
        if total >= quota:
            return True
        else:
            return False

    def compare_to(self,other):
        if self.total_sales() > other.total_sales():
            return 1
        elif self.total_sales() < other.total_sales():
            return -1
        elif self.total_sales() == other.total_sales():
            return 0

    def __str__(self):
        return "<{0}>-<{1}>: <{2}>".format((self.employee_id),(self.name),(self.total_sales()))
