from dataclasses import dataclass
from datetime import datetime
from model.plane import Plane
from model.pilot import Pilot
from model.flight_attendant import FlightAttendant


@dataclass(kw_only=True)
class Voyage:
    id: int = None
    destination: int
    sold_seats: int
    plane: Plane
    pilots: list[Pilot] = None
    flight_attendants: list[FlightAttendant] = None
    departure_time: datetime
    departure_flight: int # flight id
    arrival_departure_time: datetime
    arrival_flight: int # flight id
    date: datetime
    return_date: datetime
    status: str
    # Status options: Finished, Landed abroad, In the Air, Not started, Cancelled 
