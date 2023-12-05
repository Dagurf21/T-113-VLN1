from dataclasses import dataclass

@dataclass
class Employee:
    id = None
    name: str
    password_hash: str
    address: str
    ssn: str
    mobile_phone: str
    email: str
    home_phone: str

