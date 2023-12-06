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

from model.pilot import Pilot
from model.employee import Employee

pilot1 = Pilot(
    id=None,
    name="Manny",
    password="Mannypassword",
    ssn="ssn",
    mobile_phone="12312",
    email="Dance@gmail.com",
    address="Home",
    home_phone="Bigphone",
    license="to kill",
    assignments="kill",
)
pilot2 = Employee(
    id=None,
    name="Manny",
    password="Mannypassword",
    ssn="ssn",
    mobile_phone="12312",
    email="Dance@gmail.com",
    address="Home",
    home_phone="Bigphone",
)


pilot_list = [pilot1, pilot2]

for pilot in pilot_list:
    try:
        pilot.license
    except AttributeError:
        print(False)
print(True)
