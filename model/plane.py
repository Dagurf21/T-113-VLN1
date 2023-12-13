from dataclasses import dataclass, field

@dataclass(kw_only=True)
class Plane:
    id: int = None
    name: str
    ty: str # type
    manufacturer: str
    capacity: int
    voyages: list[int] = field(default_factory=lambda: [])
