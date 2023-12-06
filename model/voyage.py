from dataclasses import dataclass
from datetime import datetime
from model.plane import Plane
from model.pilot import Pilot
from model.flight_attendant import FlightAttendant


@dataclass(kw_only=True)
class Voyage:
    id: int = None
    sold_seats: int
    plane: Plane
    pilots: list[Pilot]
    flight_attendants: list[FlightAttendant]
    departure_flight: int
    arrival_flight: int
    date: datetime
