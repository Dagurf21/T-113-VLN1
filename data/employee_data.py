#import os
import csv
from model.employee import Employee

class Employee_Data:
    def __init__(self):
        #print(os.getcwd())
        self.file_name = "files/employees.csv"


    def read_all_employees(self):
        ret_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Employee(row["name"], row["birth_year"]))
        return ret_list


    def create_employee(self, employee):
        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["id", "name", "job_title", "password", "address", "ssn", "mobile_phone", "email", "home_phone"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            id = self.get_new_id()
            writer.writerow({'id': id, 'name': employee.name, 'job_title': employee.job_title, 'password': employee.password, 'address': employee.address, 'ssn': employee.ssn, 'mobile_phone': employee.mobile_phone, 'email': employee.email, 'home_phone': employee.home_phone})
    

    def get_new_id(self) -> int:
        """Returns the id for a new employee"""
        id = 0
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                id += 1

            return id