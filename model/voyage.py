from dataclasses import dataclass
from model.plane import Plane
from model.pilot import Pilot
from model.flight_attendant import FlightAttendant
import datetime

@dataclass(kw_only=True)
class Voyage:
    id: int = None
    destination: int
    sold_seats: int
    plane: Plane
    pilots: list[Pilot] = None
    flight_attendants: list[FlightAttendant] = None
    departure_time: datetime.time
    departure_flight: int # flight id
    arrival_departure_time: datetime.time
    arrival_flight: int # flight id
    date: datetime.date
    return_date: datetime.date
    status: str
    # Status options: Finished, Landed abroad, In the Air, Not started, Cancelled 

# TODO: Swap status for enum?
