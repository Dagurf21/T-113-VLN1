from data.employee_data import Employee_Data
from model.employee import Employee

class Employee_Logic:
    """This class is the logic layer for the employee class"""
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def create_employee(self, employee):
        """Takes in a employee object and forwards it to the data layer"""

        self.data_wrapper.create_employee(employee)

    def list_all_employees(self) -> list:
        """Returns a list of all employees"""
        return self.data_wrapper.list_all_employees()

    def list_employee(self, id):
        """Returns a employee object with the given id"""
        return self.data_wrapper.list_employee(id)

    def update_employee(self, id, data):
        """Updates a employee object with the given id"""
        self.data_wrapper.update_employee(id, data)

    def delete_employee(self, id):
        """Deletes a employee object with the given id"""
        self.data_wrapper.delete_employee(id)


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
