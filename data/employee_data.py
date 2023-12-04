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
            fieldnames = ["name", "birth_year"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({'name': employee.name, 'birth_year': employee.birth_year})