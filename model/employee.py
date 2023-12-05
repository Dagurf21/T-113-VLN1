from dataclasses import dataclass

@dataclass(kw_only=True)
class Employee:
    id: int = None
    name: str
    password: str
    address: str
    ssn: str
    mobile_phone: str
    email: str
    home_phone: str
