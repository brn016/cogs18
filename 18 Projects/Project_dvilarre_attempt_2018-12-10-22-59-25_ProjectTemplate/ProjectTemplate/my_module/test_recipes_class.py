

from recipes_class import Recipes

# Tests for the object
assert Recipes
test_recip = Recipes()
assert isinstance(test_recip, Recipes)
assert test_recip.n_recipes == 0
assert isinstance(test_recip.recipes, list)


# Tests for add_recipes method
test_inv = Recipes()
test_inv.add_recipes('Lemonade', ['Lemon','Sugar','Water'], [1,2,1], ['','Tbsp','Cup'],'Take all ingredients and them to a pitcher')
assert test_inv.n_recipes == 1
assert test_inv.recipes[0] == {'recipe': 'Lemonade', 'ingredients': ['Lemon','Sugar','Water'], 'quantity': [1,2,1], 'units':['','Tbsp','Cup'],'description':'Take all ingredients and them to a pitcher'}