from dataclasses import dataclass
from model.employee import Employee

@dataclass
class Pilot(Employee):
    license: str
    assignments: list[int]
