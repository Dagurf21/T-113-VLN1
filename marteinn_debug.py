#
#   Saman:
#         Employee_logic
#
# Marteinn:
#         Employee_logic
#         Destination_logic
#         Voyage_logic
#
# Kristján:
#         Flight_route_logic
#         Plane_logic

from model.manager import Manager

managerman = Manager(
    name="Marteinn",
    password_hash="1234",
    address="Hafnarstræti 103",
    ssn="1234567890",
    mobile_phone="1234567",
    email="",
    home_phone="",
    work_phone="1234567",
    id=1,
)

print(managerman)
