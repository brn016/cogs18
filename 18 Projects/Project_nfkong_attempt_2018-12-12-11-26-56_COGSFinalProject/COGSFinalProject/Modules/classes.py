class Animals:
    
    """Main animal class with general attributes.""" 
    
    def __init__(self, name, scientific_name, migration_distance, departure, arrival):
        
        self.name = name
        self.scientific_name = scientific_name
        self.migration_distance = migration_distance # in terms of kilometers
        self.departure = departure #migrate from...
        self.arrival = arrival #migrate to...   
        
class Fish(Animals): 
    
    """Fish class that inherits from Animals."""
    
    reason = 'Fish migrate to spawn and reproduce usually upriver to protect their eggs from predators.\n'
    
    def __init__(self, name, scientific_name, migration_distance, departure, arrival, water_type):
        
        super().__init__(name, scientific_name, migration_distance, departure, arrival)
        self.water_type = water_type
        
    def print_intro(self):
        
        """Prints a fun fact when user selects this category."""
            
        print('Did you know, that fish can migrate between freshwater and saltwater?') #opener when user selects Fish class
        
        
fish = Fish('', '', '', '', '', '')
kokanee_salmon = Fish('Kokannee Salmon', "Oncorhynchus nerka", '1000', "freshwater lakes around Yukon Canada", "spawning grounds upriver", "Fresh water")
golden_dorado = Fish('Golden Dorado', "Salminus brasiliensis", "400", "Paraguay River", "spawning grounds upstream", "Fresh water")
mekong_giant_catfish = Fish('Mekong Giant Catfish', "Pangasianodon gigas", "2600", 'Tonle Sap lake', "Cambodian Meekong River", "Fresh water")
fish_set = [kokanee_salmon, golden_dorado, mekong_giant_catfish]



class Bird(Animals):
    
    """Bird class that inherits from Animals."""
    
    reason = 'Birds will migrate alongside insects to feed on them and to find nesting grounds.'
    
    def __init__(self, name, scientific_name, migration_distance, departure, arrival):
        
        super().__init__(name, scientific_name, migration_distance, departure, arrival)
        
    def print_intro(self):
        
        """Prints a fun fact when user selects this category."""
        
        print('Did you know that birds hold the record for longest animal migrations?')
        
              
bird = Bird('', '', '', '', '')
calliope_hummingbird = Bird('Calliope Hummingbird', 'Psaltriparus minimus', '4500', 'Northwestern North America', 'Mexico')
arctic_tern = Bird('Arctic Tern', 'Sterna paradisaea', '90000', 'the Arctic region', 'Antarctica')
peregrine_falcon = Bird('Peregrine Falcon', 'Falco peregrinus', '25000', 'Canada', 'Southern United States')
bird_set = [calliope_hummingbird, arctic_tern, peregrine_falcon]
              
              
              
class Mammal(Animals):
    
    """Mammal class that inherits from Animals."""
    
    reason = 'Mammals migrate following food patterns that are governed by the weather and to find birthing grounds.'
              
    def __init__(self, name, scientific_name, migration_distance, departure, arrival):
        super().__init__(name, scientific_name, migration_distance, departure, arrival)
    
    def print_intro(self):
        
        """Prints a fun fact when user selects this category."""
              
        print('Did you know mammals tend to have the shortest migration routes because walking takes more energy than flying or swimming?')
              
mammal = Mammal('', '', '', '', '')
wildebeest = Mammal('Wildebeest', 'Connochaetes', '2900', 'south Serengeti plains in December', 'Masai Mara, Kenya in September after crossing the Grumeti River in July')
porcupine_caribou = Mammal('Porcupine Caribou', 'Rangifer tarandus granti', '2400', 'southern Brooks Range in Alaska and Yukon, Canada' , 'the Porcupine River in the Arctic National Wildlife refuge')
blue_whale = Mammal('Blue Whale', 'Balaenoptera musculus', '5000', 'southern Chile in the winter after feeding', 'the Galapagos Islands or closer to the equater to find birthing grounds')
mammal_set = [wildebeest, porcupine_caribou, blue_whale]
              
class Insect(Animals):
    
    """Insect class that inherits from Animals."""
    
    reason = 'Insects in the Americas migrate South because they are unable to withstand the cold winter winds in the North.'
    
    def __init__(self, name, scientific_name, migration_distance, departure, arrival):
        super().__init__(name, scientific_name, migration_distance, departure, arrival)
        #departure: "from...departure"
        #arrival: "to...arrival"
                
    def print_intro(self):
        
        """Prints a fun fact when user selects this category."""
        
        print("Did you know that most insect migrations are intergenerational, meaning that offspring continue their parent's journey?\n")
    
insect = Insect('', '', '', '', '')
monarch_butterfly = Insect('Monarch Butterfly', 'Danaus plexippus', '4800', 'southern Canada', 'central Mexico')
wandering_glider = Insect('Wandering Glider', 'Pantala flavescens', '16000', 'southern India', 'south and east Africa')
potato_leafhopper = Insect('Potato Leafhopper', 'Empoasca fabae', '2500', 'the Midwest and southern Canada', 'Gulf of Mexico and Southern United States')
insect_set = [monarch_butterfly, wandering_glider, potato_leafhopper]








