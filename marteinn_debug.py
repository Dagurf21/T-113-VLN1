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
    1, "man", "siaebhe", "home", "ssn", "mobile", "email", "home", "work"
)

print(managerman)
