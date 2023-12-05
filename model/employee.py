from dataclasses import dataclass

@dataclass
class Employee:
    id: int = None
    name: str
    job_title: str
    password_hash: str
    address: str
    ssn: str
    mobile_phone: str
    email: str
    home_phone: str