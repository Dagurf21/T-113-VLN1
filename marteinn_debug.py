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
import datetime


def validate_ssn(ssn):
    day, month, year, random, check_digit, century = (
        int(ssn[0:2]),
        int(ssn[2:4]),
        int(ssn[4:6]),
        int(ssn[6:8]),
        int(ssn[8:9]),
        int(ssn[9:10]),
    )
    try:
        datetime.date(day, month, year)
        return True
    except ValueError:
        return False


print(validate_ssn("05090483k3"))
