from dataclasses import dataclass
from model import Employee


@dataclass(kw_only=True)
class Pilot(Employee):
    license: str
    assignments: list[int]

    def __lt__(self, other_pilot):
        """This makes it so that the logic layer can
        sort by liscense"""
        return self.license < other_pilot.license
