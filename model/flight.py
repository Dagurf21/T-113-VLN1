from dataclasses import dataclass
from datetime import datetime

@dataclass(kw_only=True)
class Flight:
    flight_number: str
    departure: int
    destination: int
    date: datetime
    departure_time: str
    arrival_time: str
