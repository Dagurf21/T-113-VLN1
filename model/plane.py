from dataclasses import dataclass, field

@dataclass(kw_only=True)
class Plane:
    id: int = None
    name: str
    ty: str
    manufacturer: str
    capacity: int
    flights: list[int] = field(default_factory=lambda: [])
