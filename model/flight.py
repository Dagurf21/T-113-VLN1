from dataclasses import dataclass
import datetime

@dataclass(kw_only=True)
class Flight:
    flight_number: str
    departure: int
    destination: int
    date: datetime.date
    departure_time: str
    arrival_time: str
