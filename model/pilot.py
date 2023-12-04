from dataclasses import dataclass
from model.employee import Employee

@dataclass
class Pilot:
    license: str
    assignments: List[int]
