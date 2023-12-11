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


class bobs:
    def __init__(self, liscense) -> None:
        self.bob_liscense = liscense

    def __str__(self) -> str:
        return "Bob" + self.bob_liscense

    def __lt__(self, enemy_bob) -> bool:
        return self.bob_liscense < enemy_bob.bob_liscense


bob_list = [bobs("Gogo"), bobs("Gege"), bobs("Gaga")]

sort_list = sorted(bob_list)

for x in bob_list:
    print(x)

for x in sort_list:
    print(x)
