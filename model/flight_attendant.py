from dataclasses import dataclass
from model.employee import Employee

@dataclass
class Employee:
    assignments: List[int]

