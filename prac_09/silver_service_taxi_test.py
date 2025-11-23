from silver_service_taxi import SilverServiceTaxi

# Create taxi: name, fuel, fanciness
taxi = SilverServiceTaxi("Hummer", 200, 4)

# Drive 18 km
taxi.start_fare()
taxi.drive(18)

# Calculate fare
fare = taxi.get_fare()