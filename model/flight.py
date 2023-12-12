from dataclasses import dataclass
import datetime

@dataclass(kw_only=True)
class Flight:
    flight_number: str
    departure: int
    destination: int
    date: datetime
    departure_time: datetime
    arrival_time: datetime
