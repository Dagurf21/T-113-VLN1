from dataclasses import dataclass
from model.employee import Employee

@dataclass
class FlightManager(Employee):
    work_phone: str

