from dataclasses import dataclass

@dataclass
class FlightRoute:
    id = None
    flight_number: str
    departure: int
    destination: int
    departure_time: str
    arrival_time: str

