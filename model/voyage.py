from dataclasses import dataclass
from datetime import datetime

@dataclass
class Voyage:
    id = None
    sold_seats: int
    plane: int
    departure_flight: int
    arrival_flight: int
    date: datetime

