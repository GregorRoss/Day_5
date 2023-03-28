pet_shop = {
    "pets": [
        {
            "name": "Sir Percy",
            "pet_type": "cat",
            "breed": "British Shorthair",
            "price": 500
        },
        {
            "name": "King Bagdemagus",
            "pet_type": "cat",
            "breed": "British Shorthair",
            "price": 500
        },
        {
            "name": "Sir Lancelot",
            "pet_type": "dog",
            "breed": "Pomsky",
            "price": 1000,
        },
        {
            "name": "Arthur",
            "pet_type": "dog",
            "breed": "Husky",
            "price": 900,
        },
        {
            "name": "Tristan",
            "pet_type": "cat",
            "breed": "Basset Hound",
            "price": 800,
        },
        {
            "name": "Merlin",
            "pet_type": "cat",
            "breed": "Egyptian Mau",
            "price": 1500,
        }
    ],
    "admin": {
        "total_cash": 1000,
        "pets_sold": 0,
    },
    "name": "Camelot of Pets"
}

new_pet = {
            "name": "Bors the Younger",
            "pet_type": "cat",
            "breed": "Cornish Rex",
            "price": 100
        }


customers = [
            {
                "name": "Alice",
                "pets": [],
                "cash": 1000
            },
            {
                "name": "Bob",
                "pets": [],
                "cash": 50
            },
            {
                "name": "Jack",
                "pets": [],
                "cash": 100
            }
        ]

#print(type(customers))
#print(customers)
#customer = customers[0]
#print(type(customer))
#print(customer)
#cust_pet = customer["pets"]
#print(type(cust_pet))
#print(cust_pet)
#customer["pets"].append(new_pet)
#cust_pet.append(new_pet)
#print(cust_pet)
#print(customer)
#print(new_pet)

# valid_purchase = False
# if customer["cash"] >= new_pet["price"]:
#     valid_purchase = True
# else:
#     valid_purchase = False

# print(valid_purchase)

# for pet in pet_shop["pets"]:
#     if pet["name"] == "Arthur":
#         cost = pet["price"]
# pets = pet_shop["pets"]
# print(type(pet_shop))
# print(pet_shop["pets"][0])
# print(type(pets))
# print(pets)
# print(cost)
# print(customers[0])
# print(customers[0]["cash"])

print(pet_shop['pets'])
# name = "Arthur"
# for pet in pet_shop["pets"]:
#     print(pet.index("name"))
#     if pet["name"] == name:
#         del pet["name"]
# print(pet_shop['pets'])
pets = pet_shop["pets"]
print(pets.index)
