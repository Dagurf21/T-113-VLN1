from dataclasses import dataclass

@dataclass(kw_only=True)
class Flight:
    id: int = None
    flight_number: str
    departure: int
    destination: int
    departure_time: str
    arrival_time: str

