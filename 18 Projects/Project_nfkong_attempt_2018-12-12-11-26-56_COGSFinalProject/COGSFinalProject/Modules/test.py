# Test to make sure classes work
assert Fish

name = 'blue fish'
scientific_name = 'fish fish'
migration_distance = '310'
departure = 'Los Angeles'
arrival = 'New York'
water_type = 'salt'

animal_test = Fish(name, scientific_name, migration_distance, departure, arrival, water_type)
assert isinstance(animal_test, Fish)

assert animal_test.reason == 'Fish migrate to spawn and reproduce usually upriver to protect their eggs from predators.\n'
assert animal_test.name == name
assert animal_test.scientific_name == scientific_name
assert animal_test.migration_distance == migration_distance
assert animal_test.departure == departure
assert animal_test.arrival == arrival
assert animal_test.water_type  == water_type 

assert animal_test.print_intro() == 'Did you know, that fish can migrate between freshwater and saltwater?'