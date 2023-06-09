# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]


# Function to get total Cash
def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

# Function to add or remove cash
## this function does not return a value just modifies the data
def add_or_remove_cash(pet_shop,amount):
    pet_shop["admin"]["total_cash"] += amount
 
# Function to get pets that have been sold
def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]


# Function to increase the number of pets that have been sold
def increase_pets_sold(pet_shop,num1):
    pet_shop["admin"]["pets_sold"] += num1

# Function to get the stock count of pets
def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

# Function to get pets by breed
def get_pets_by_breed(pet_shop,breed):
    found_breed = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            found_breed.append(pet)
    return found_breed

# Function to get pet by name
def find_pet_by_name(pet_shop,name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet

# Function to remove pet by name
#
# add the remove using the function above
#
# return pet_shop{"pets"}.remove()
#
def remove_pet_by_name(pet_shop,name):
   pet_delete = find_pet_by_name(pet_shop,name)
   pet_shop['pets'].remove(pet_delete)



# Function to add pet to stock
def add_pet_to_stock(pet_shop,new_stock):
    pet_shop["pets"].append(new_stock)

# Function to get customer cash
def get_customer_cash(customer):
    return(customer["cash"])

# Function to remove customer cash
def remove_customer_cash(customer, cash):
    customer["cash"] -= cash

# Function to get customer count
def  get_customer_pet_count(customer):
    return(len(customer["pets"]))

# function to add pet to customer
def add_pet_to_customer(customer, pet):
        customer["pets"].append(pet)

# Function to confirm if customer can afford pet
def customer_can_afford_pet(customer, pet):
    valid_purchase = False
    if customer["cash"] >= pet["price"]:
        valid_purchase = True
    else:
        valid_purchase = False

    return(valid_purchase)



# Function sell pet to customer
def sell_pet_to_customer(pet_shop,pet,customer):
    if pet != None and customer_can_afford_pet(customer,pet):
        remove_customer_cash(customer,pet["price"])
        add_or_remove_cash(pet_shop,pet["price"])
        add_pet_to_customer(customer,pet)
        remove_pet_by_name(pet_shop,pet["name"])
        increase_pets_sold(pet_shop,1)
    Else: print("Pet not Found")




