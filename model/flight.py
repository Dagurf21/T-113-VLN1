from dataclasses import dataclass

@dataclass(kw_only=True)
class Flight:
    flight_number: str
    departure: int
    destination: int
    departure_time: str
    arrival_time: str

