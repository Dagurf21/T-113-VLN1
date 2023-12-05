from dataclasses import dataclass

@dataclass(kw_only=True)
class Destination:
    id: int = None
    country: str
    airport: str
    distance_km: int
    flight_time: int
    representatie: str
    emergency_number: str
