from dataclasses import dataclass
from datetime import datetime
from model.plane import Plane


@dataclass(kw_only=True)
class Voyage:
    id: int = None
    sold_seats: int
    plane: Plane
    departure_flight: int
    arrival_flight: int
    date: datetime
