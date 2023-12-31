from dataclasses import dataclass
from model import Employee

@dataclass(kw_only=True)
class FlightAttendant(Employee):
    assignments: list[int]
