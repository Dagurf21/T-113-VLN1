from logic.validator_logic import Validator

VALIDATION_ERRORS = (
    "Invalid SSN. ",
    "Invalid Phone Number. ",
    "Invalid Email. ",
    "Invalid Home Number. ",
)


class EmployeeLogic:
    """This class is the logic layer for the employee class"""

    def __init__(self, data_connection):
        self.data_wrapper = data_connection
        self.validate = Validator()

    def create_employee(self, employee):
        """Takes in a employee object and forwards it to the data layer"""
        error_check = self.validate_employee(employee)
        if error_check is "":
            return self.data_wrapper.create_employee(employee)
        else:
            raise ValueError(error_check)

    def list_all_employees(self) -> list:
        """Returns a list of all employees"""
        employee_list = self.data_wrapper.get_all_employees()
        # Sorting and tomfoolery
        return employee_list

    def get_employee(self, id):
        """Returns a employee object with the given id"""
        employee = self.data_wrapper.get_employee(id)

        return employee

    def get_employee_by_email(self, email):
        """Returns a employee object with the given id"""
        employee = self.data_wrapper.get_employee_by_email(email)

        return employee

    def update_employee(self, employee):
        """Updates a employee object with the given id"""
        error_check = self.validate_employee(employee)
        # Commence sorting!
        if error_check is "":
            return self.data_wrapper.update_employee(employee)
        else:
            raise ValueError(error_check)

    def delete_employee(self, id):
        """Deletes a employee object with the given id"""
        return self.data_wrapper.delete_employee(id)

    def validate_employee(self, employee):
        """Validates a given employee"""
        list_of_outcomes = []

        list_of_outcomes.append(self.validate.ssn(employee.ssn))
        list_of_outcomes.append(self.validate.phone_number(employee.mobile_phone))
        list_of_outcomes.append(self.validate.email(employee.email))
        if employee.home_phone is None:
            list_of_outcomes.append(True)
        else:
            list_of_outcomes.append(self.validate.phone_number(employee.home_phone))

        error_message = ""

        for x in range(4):
            if list_of_outcomes[x] is False:
                error_message += VALIDATION_ERRORS[x]

        return error_message
