print("(6-1 Person)\n")

person_info = {
    "first_name": "josh",
    "last_name": "miller",
    "age": 37,
    "city": "broomfield",
}

print(person_info["first_name"])
print(person_info["last_name"])
print(person_info["age"])
print(person_info["city"])

print("\n")

print("(6-2 Favorite Numbers)\n")

fav_numbers = {
    "Josh": 52,
    "Kalina": 33,
    "Cora": 5,
    "Trevor": 46,
    "Vong": 15,
}

print(f"Josh's favorite number is {fav_numbers['Josh']}")
print(f"Kalina's favorite number is {fav_numbers['Kalina']}")
print(f"Cora's favorite number is {fav_numbers['Cora']}")
print(f"Trevor's favorite number is {fav_numbers['Trevor']}")
print(f"Vong's favorite number is {fav_numbers['Vong']}")

print("\n")

print("6-2 in a for loop")
for name, num in fav_numbers.items():
    print(f"{name.title()}'s favorite number is {num}")
print("\n")
# print('(6-3 Glossary)')

# More of the same as above

# Information Section

"""
Using the .items() pulls both the Keys and Values
Using the .keys() pulls the Keys - Keys are the default used in a loop.  .keys() is not required but could make things more clear.
Using the .values() pulls the Values
"""

print("Looping through dictionary")

user_0 = {
    "username": "Silentgimp",
    "fist": "Josh",
    "last": "Miller",
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

