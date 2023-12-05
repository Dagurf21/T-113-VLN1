from dataclasses import dataclass
from model.employee import Employee

@dataclass(kw_only=True)
class Pilot(Employee):
    license: str
    assignments: list[int]
