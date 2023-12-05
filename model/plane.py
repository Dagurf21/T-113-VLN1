from dataclasses import dataclass

@dataclass
class Plane:
    id = None
    name: str
    ty: str
    manufacturer: str
    capacity: int
    flights: list[int]

