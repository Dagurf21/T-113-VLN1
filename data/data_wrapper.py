from data.employee_data import Employee_Data


class Data_Wrapper:
    def __init__(self):
        self.employee_data = Employee_Data()

    def get_all_employees(self):
        return self.employee_data.read_all_employee()

    def create_customer(self, employee):
        return self.employee_data.create_employee(employee)