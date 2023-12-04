
class Employee_Logic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def create_employee(self, employee):
        """Takes in a employee object and forwards it to the data layer"""

        self.data_wrapper.create_employee(employee)

    def list_all_employees(self):
        return self.data_wrapper.get_all_employees()

'''
from data.customer_data import Customer_Data
from model.customer import Customer

class Customer_Logic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def create_customer(self, customer):
        """Takes in a customer object and forwards it to the data layer"""

        self.data_wrapper.create_customer(customer)

    def get_all_customers(self):
        return self.data_wrapper.get_all_customers()
'''