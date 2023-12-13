from dataclasses import dataclass, field
import datetime
from model.plane import Plane
from model.pilot import Pilot
from model.flight_attendant import FlightAttendant
import enum

class VoyageStatus(enum.StrEnum):
    Cancelled = "Cancelled",
    NotStarted = "Not Started",
    InTheAir = "In the Air",
    LandedAbroad = "Landed Abroad",
    Finished = "Finished",

@dataclass(kw_only=True)
class Voyage:
    id: int = None
    destination: int
    sold_seats: int
    plane: Plane
    pilots: list[Pilot] = field(default_factory=lambda: [])
    flight_attendants: list[FlightAttendant] = field(default_factory=lambda: [])
    departure_time: datetime.time
    departure_flight: str # flight id
    departure_date: datetime.date
    return_departure_time: datetime.time
    return_flight: str # flight id
    return_date: datetime.date
    status: VoyageStatus
