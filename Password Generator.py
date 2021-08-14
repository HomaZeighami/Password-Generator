# Python Random Module.
import random
import string

# The user's input for the length of password.
password_length = int(input("How long do you want your password to be? "))
password = ""

# For each position up to the length of the password,
# the program comes up with a random letter and adds that to the existing password.
for position in range(password_length):
    password = password + random.choice(string.ascii_letters)

print(password)
