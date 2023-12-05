from dataclasses import dataclass

@dataclass
class Destination:
    country: str
    airport: str
    distance_km: int
    flight_time: int
    representatie: str
    emergency_number: str
