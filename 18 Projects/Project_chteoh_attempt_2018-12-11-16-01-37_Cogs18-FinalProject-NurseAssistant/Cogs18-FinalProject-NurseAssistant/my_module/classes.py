#define a class called Patient, of which instances of the class can be created.
class Patient():
    
    #Initializer, which allows us to specify instance-specific attributes
    def __init__(self, name, age, height, weight, cholesterol_level, blood_pressure): 
          
        #Initialize instance attributes 
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.cholesterol_level = cholesterol_level
        self.blood_pressure = blood_pressure
        