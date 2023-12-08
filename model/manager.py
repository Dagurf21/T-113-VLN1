from dataclasses import dataclass
from model.employee import Employee

@dataclass(kw_only=True)
class Manager(Employee):
    work_phone: str
