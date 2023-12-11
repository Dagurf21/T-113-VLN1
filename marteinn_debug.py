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
password = "123"

# converting password to array of bytes
bbytes = password.encode("utf-8")

# generating the salt
salt = bcrypt.gensalt()

# Hashing the password
hash = bcrypt.hashpw(bbytes, salt)

print(hash)
decoded = hash.decode("utf-8")
print(decoded)
encoded = decoded.encode("utf-8")
print(encoded)

# Taking user entered password
userPassword = "123"

# encoding user password
userBytes = userPassword.encode("utf-8")

# checking password
result = bcrypt.checkpw(userBytes, decoded)

print(result)
