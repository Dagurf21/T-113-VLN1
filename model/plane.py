from dataclasses import dataclass

@dataclass
class Plane:
    name: str
    ty: str
    manufacturer: str
    capacity: int
    flights: List[int]

