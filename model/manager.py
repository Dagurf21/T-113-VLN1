from dataclasses import dataclass
from model.employee import Employee

@dataclass
class Manager(Employee):
    work_phone: str

