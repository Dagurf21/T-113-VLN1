from dataclasses import dataclass, field
from model import Employee


@dataclass(kw_only=True)
class Pilot(Employee):
    license: str
    assignments: list[int] = field(default_factory=lambda: [])

