from dataclasses import dataclass
from model.employee import Employee

@dataclass
class FlightAttendant(Employee):
    assignments: List[int]

