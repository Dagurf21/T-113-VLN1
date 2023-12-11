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


import bcrypt

# example password
password = "passwordabc"

# converting password to array of bytes
bytes = password.encode("utf-8")

# generating the salt
salt = bcrypt.gensalt()

# Hashing the password
hash = bcrypt.hashpw(bytes, salt)

# Taking user entered password
userPassword = "passwordabc"

# encoding user password
userBytes = userPassword.encode("utf-8")

# checking password
result = bcrypt.checkpw(userBytes, hash)

print(result)
