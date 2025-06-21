# Inventory system using a dictionary

inventory = {
    "Lamborghini Aventador": 3,
    "Ferrari SF90 Stradale": 2,
    "Bugatti Chiron": 1,
    "McLaren 720S": 4,
    "Porsche 911 Turbo S": 5,
    "Mercedes G-Wagon": 3,
    "Land Rover Defender": 2,
    "BMW X7": 4,
}

# Display the inventory
print("🏁 Current Inventory:\n")
for car, quantity in inventory.items():
    print(f"{car}: {quantity} units")