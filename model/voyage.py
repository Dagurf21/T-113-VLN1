from dataclasses import dataclass
import datetime
from model.plane import Plane
from model.pilot import Pilot
from model.flight_attendant import FlightAttendant
import enum

@dataclass(kw_only=True)
class Voyage:
    id: int = None
    destination: int
    sold_seats: int
    plane: Plane
    pilots: list[Pilot] = None
    flight_attendants: list[FlightAttendant] = None
    departure_time: datetime.datetime
    departure_flight: str # flight id
    arrival_departure_time: datetime.datetime
    arrival_flight: str # flight id
    date: datetime.datetime
    return_date: datetime.datetime
    status: VoyageStatus
    # Status options: Finished, Landed abroad, In the Air, Not started, Cancelled 

class VoyageStatus(enum.Enum):
    Cancelled,
    NotStarted,
    InTheAir,
    LandedAbroad,
    Finished,

# TODO: Swap status for enum?
