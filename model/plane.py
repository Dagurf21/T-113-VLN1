from dataclasses import dataclass

@dataclass(kw_only=True)
class Plane:
    id: int = None
    name: str
    ty: str
    manufacturer: str
    capacity: int
    flights: list[int]

