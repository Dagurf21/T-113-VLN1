from data.employee_data import Employee_Data
from model.employee import Employee
from model.flight_attendant import FlightAttendant
from model.pilot import Pilot
from model.flight_manager import FlightManager
from model.manager import Manager


class EmployeeLogic:
    """This class is the logic layer for the employee class"""

    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def create_employee(self, employee_data):
        """Takes in a employee object and forwards it to the data layer"""
        employee = self.make_employee_class(employee_data)

        return self.data_wrapper.create_employee(employee)

    def list_all_employees(self) -> list:
        """Returns a list of all employees"""
        employee_list = self.data_wrapper.list_all_employees()
        # Sorting and tomfoolery
        return employee_list

    def list_employee(self, id):
        """Returns a employee object with the given id"""
        employee = self.data_wrapper.list_employee(id)
        return employee

    def update_employee(self, id, data):
        """Updates a employee object with the given id"""
        employee = self.make_employee_class(data, id)

        return self.data_wrapper.update_employee(employee)

    def delete_employee(self, id):
        """Deletes a employee object with the given id"""
        return self.data_wrapper.delete_employee(id)

    def make_employee_class(self, employee_data, employee_id=None):
        """Creates a employee object with the given data and returns it"""
        name, password, address, ssn, mobile_phone, email, home_phone = employee_data
        employee = Manager(
            id=employee_id,
            name=name,
            password_hash=password,
            address=address,
            ssn=ssn,
            mobile_phone=mobile_phone,
            email=email,
            home_phone=home_phone,
            work_phone="1234567",
        )
        return employee


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
