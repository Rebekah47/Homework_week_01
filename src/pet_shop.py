# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, amount):
    current_total = get_total_cash(pet_shop)
    new_total = current_total + amount
    pet_shop["admin"]["total_cash"] = new_total

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, increase):
    current_pets = get_pets_sold(pet_shop)
    new_pets = current_pets + increase
    pet_shop["admin"]["pets_sold"] = new_pets

def get_stock_count(pet_shop):
     return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed_type):
    pet_breed = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed_type:
            pet_breed.append(pet)
    return pet_breed

def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet

# def remove_pet_by_name(pet_shop, pet_name):
#     for pet in pet_shop["pets"]:
#         if pet["name"] == pet_name:
#             del pet 

# def remove_pet_by_name(pet_shop, pet_name):
#     removed_pet = []
#     for pet in pet_shop["pets"]:
#         if pet["name"] == pet_name:
#             del pet
#             removed_pet.append(pet)
#             return removed_pet

def remove_pet_by_name(pet_shop, pet_name):
    current_pet = find_pet_by_name(pet_shop, pet_name)
    removed_pet = pet_shop["pets"].remove(current_pet)
    return removed_pet

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, amount):
    current_cash = get_customer_cash(customer)
    new_cash = current_cash - amount
    customer["cash"] = new_cash
    return new_cash

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)

#Optional Extentsion

def get_pet_price(pet):
    return pet["price"]

def customer_can_afford_pet(customers, new_pet):
    current_cash = get_customer_cash(customers)
    pet_price = get_pet_price(new_pet)
    if pet_price <= current_cash:
        return True
    
    return False

#Itergration tests

def sell_pet_to_customer(pet_shop, pet, customer):
    if pet:
        if customer_can_afford_pet(customer, pet):
            add_pet_to_customer(customer, pet)
            increase_pets_sold(pet_shop, 1)
            remove_customer_cash(customer, get_pet_price(pet))
            add_or_remove_cash(pet_shop, get_pet_price(pet))


# def sell_pet_to_customer(pet_shop, pet, customers):
#     if pet:
#         if customer_can_afford_pet(customers, pet):
#             add_pet_to_customer(customers, pet)
#             increase_pets_sold(pet_shop, 1)
#             remove_customer_cash(customers, get_pet_price(pet))
#             add_or_remove_cash(pet_shop, get_pet_price(pet))
            
            

            