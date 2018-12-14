

class Recipes():
    
    def __init__(self):
        self.recipes = []
        self.n_recipes = 0
        
    def add_recipes(self,recipe,ingredients,quantity,units,description):
        """
        recipe : string
        ingredients : list
        quantity : list
        units : list
        description : string
        """
        self.recipes.append({
            'recipe':recipe,
            'ingredients':ingredients,
            'quantity':quantity,
            'units':units,
            'description':description
        })
        self.n_recipes += 1
    
    def save_to_file(self):
        #Save inputted dictionaries for later use
        file = open("recipes_list.txt", "w") 
        for i in self.recipes:
            file.write(str(i))
        
        file.close()
        
    def load_file(self):
        #Load saved file to edit
        load_file = open("recipes_list.txt", "r")
        out = load_file.readlines()