from dataclasses import dataclass
import datetime
import enum

class FlightStatus(enum.StrEnum):
    Available = "Available"
    InUse     = "In Use"

@dataclass(kw_only=True)
class Flight:
    flight_number: str
    departure: int
    destination: int
    date: datetime.date
    departure_time: datetime.time
    arrival_time: datetime.time
