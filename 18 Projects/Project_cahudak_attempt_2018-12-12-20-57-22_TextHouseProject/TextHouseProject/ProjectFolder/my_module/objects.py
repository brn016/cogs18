
class ThingsInventory():
    """ Keeps track of inventory of things/object in rooms, can be used to add things to rooms,
        and find a specific thing from the list of things in the room 
        
    Attributes
    ----------
    list_of_things : list of strings
            objects added to the room stored as strings
            
    number_of_things : integer
    
    Methods
    -------
    add_thing(self, input_things)
            allows programmer to add object/thing to a room's list_of_things
            
    get_thing(self, input_string)
            loops through user input string to find an object/thing in a room's list_of_things
            returns "unknown" is object/thing not found in List_of_things
    """
    
    def __init__(self):
        self.list_of_things = []
        self.number_of_things = 0
        
        
    def add_thing(self, input_thing):
        
        self.list_of_things.append(input_thing)
        self.number_of_things = self.number_of_things + 1
        
    
    def get_thing(self, input_string):
        
        counter = 0
        keep_looping = True
        
        for item in self.list_of_things:
            if item in input_string:
                thing = item
                return thing
                keep_looping = False
                break
            else:
                counter = counter + 1
                
        if counter >= self.number_of_things:
            thing = "unknown"
            keep_looping = False
            return thing
        
        
class Chair():
    """ Makes a chair which can be added to a room's inventory
    
    Attributes
    ----------
    available_actions : list of strings
    
    number _of_actions : integer
    
    color : string
            describes chair
    
    texture : string
            describes chair
            
    Methods
    -------
    take_action(self, input_string)
            loops through user's input string find a matching action in available_actions
            then returns string output describing the action performed      
    """
    available_actions = ["sit", "sat", "move", "moving"]
    number_of_actions = 4
    
    def __init__(self, color, texture):
        
        self.color = color
        self.texture = texture
        
    def take_action(self, input_string):
        counter = 0
        keep_looping = True

        while keep_looping:
    
            for element in self.available_actions:
                if element in input_string:
                    action = element
                    keep_looping = False
                    break
            
                else:
                    counter = counter + 1
                
            if counter >= self.number_of_actions:
                action = "unknown action"
                keep_looping = False
                
        if action == "sit" or action == "sat":
            print ("\nYou sat down in the {} {} chair. \n".format(self.color, self.texture))
        elif action == "move" or action == "moving":
            print ("\nYou tried to move the {} {} chair and it fell over. \n".format(self.color, self.texture))
        elif action == "unknown action":
            print("\nSorry, you can't do that! \n")
            
            
class Lamp():
    """ Makes a lamp which can be added to a room's inventory
    
    Attributes
    ----------
    available_actions : list of strings
    
    number _of_actions : integer
    
    brightness : string
            describes lamp
    
    style : string
            describes lamp
            
    Methods
    -------
    take_action(self, input_string)
            loops through user's input string find a matching action in available_actions
            then returns string output describing the action performed
            
    """
    available_actions = ["on", "off", "move", "moving"]
    number_of_actions = 4
    
    def __init__(self, brightness, style):
        
        self.brightness = brightness
        self.style = style
        
    def take_action(self, input_string):
        counter = 0
        keep_looping = True

        while keep_looping:
    
            for element in self.available_actions:
                if element in input_string:
                    action = element
                    keep_looping = False
                    break
            
                else:
                    counter = counter + 1
                
            if counter >= self.number_of_actions:
                action = "unknown action"
                keep_looping = False
                
        if action == "on":
            print ("\nYou turned on the {} {} lamp. \n".format(self.brightness, self.style))
        elif action == "off":
            print ("\nYou turned off the {} {} lamp. \n".format(self.brightness, self.style))
        elif action == "move" or action == "moving":
            print ("\nI guess the lamp looks better over there. \n")
        elif action == "unknown action":
            print("\nSorry, you can't do that! \n") 
            
class Bed():
    """ Makes a bed which can be added to a room's inventory
    
    Attributes
    ----------
    available_actions : list of strings
    
    number _of_actions : integer
    
    softness : string
            describes bed
    
    material : string
            describes bed
            
    Methods
    -------
    take_action(self, input_string)
            loops through user's input string find a matching action in available_actions
            then returns string output describing the action performed      
    """
    available_actions = ["lay", "sit", "nap", "sleep"]
    number_of_actions = 4
    
    def __init__(self, softness, material):
        
        self.softness = softness
        self.material = material
        
    def take_action(self, input_string):
        counter = 0
        keep_looping = True

        while keep_looping:
    
            for element in self.available_actions:
                if element in input_string:
                    action = element
                    keep_looping = False
                    break
            
                else:
                    counter = counter + 1
                
            if counter >= self.number_of_actions:
                action = "unknown action"
                keep_looping = False
                
        if action == "lay":
            print ("\nYou laid down on the {} {} bed. \n".format(self.softness, self.material))
        elif action == "sit":
            print ("\nYou sat down on the {} {} bed. \n".format(self.softness, self.material))
        elif action == "nap":
            print ("\nYou took a short nap on the {} {} bed then woke up. \n".format(self.softness, self.material))
        elif action == "sleep":
            print ("\nYou fell asleep on the {} {} bed and woke up about 8 hours later. \n".format(self.softness, self.material))
        elif action == "unknown action":
            print("\nSorry, you can't do that! \n")
            
class Book():
    """ Makes a book which can be added to a room's inventory
    
    Attributes
    ----------
    available_actions : list of strings
    
    number _of_actions : integer
    
    heft : string
            describes book
    
    title : string
            describes book
            
    Methods
    -------
    take_action(self, input_string)
            loops through user's input string find a matching action in available_actions
            then returns string output describing the action performed        
    """
    available_actions = ["look", "read", "move", "hold"]
    number_of_actions = 4
    
    def __init__(self, title, heft):
        
        self.title = title
        self.heft = heft
        
    def take_action(self, input_string):
        counter = 0
        keep_looping = True

        while keep_looping:
    
            for element in self.available_actions:
                if element in input_string:
                    action = element
                    keep_looping = False
                    break
            
                else:
                    counter = counter + 1
                
            if counter >= self.number_of_actions:
                action = "unknown action"
                keep_looping = False
                
        if action == "look":
            print ("\nYou look at the book, the cover reads: {}. \n".format(self.title))
        elif action == "read":
            print ("\nYou read a couple pages of my book. It's one of my favorites. \n")
        elif action == "hold":
            print ("\nYou pick up the {} book and look it over. \n".format(self.heft))
        elif action == "move":
            print ("\nYou move my {} book. I hope I can find it later. \n".format(self.heft))
        elif action == "unknown action":
            print("\nSorry, you can't do that! \n")