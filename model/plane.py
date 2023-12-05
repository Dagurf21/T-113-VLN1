from dataclasses import dataclass

@dataclass
class Plane:
    id: int = None
    name: str
    ty: str
    manufacturer: str
    capacity: int
    flights: list[int]

