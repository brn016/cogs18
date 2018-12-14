#first line opening when chat starts
def chat_opening():
    
    """Prints an opening line and checks if user returns proper response to determine if the chatbot should be started."""
    
    msg = input("Would you like to learn about how animals migrate throughout and across the world? [Y/N]\nINPUT: ")
    msg = msg.lower()
    possible_replies = ['yes', 'y', 'sure', 'okay', 'yeah']
    
    for reply in possible_replies:
        
        if msg == reply:
            
            return True
        
    return False

#main menu that includes only animal categories
def print_menu():
    
    """Prints main categories of animals"""
    
    animal_menu = {'1': 'Fish', '2': 'Birds', '3': 'Mammals', '4': 'Insects', '5': 'Exit'}
    print('Learn about Animal Migration Patterns!!\nChoose a category...')
    
    for key in animal_menu:
        
        print(key + ". " + animal_menu[key])

def menu_choice():
    
    """Checks what category user wants and sets a variable equal to a list of animals for that specific category. 
    Returns True if user selects an animal category and continues asking if something other than numbers isn't inputted"""
    
    loop = chat_opening()
    if loop == False:
        return [None, None, False]
    
    while loop:
        
        print_menu()
        choice = input('INPUT: ')                                 
        
        #choice needs to equate to a string because input takes string and not int   
        if choice == '1':
            
            fish.print_intro()
            animal = 'fish'
            animal_set = fish_set
            return [animal, animal_set, True]
            break
            
        elif choice == '2':
            
            bird.print_intro()
            animal = 'bird'
            animal_set = bird_set
            return [animal, animal_set, True]
            break
            
        elif choice == '3':
            
            mammal.print_intro()
            animal = 'mammal'
            animal_set = mammal_set
            return [animal, animal_set, True]
            break
            
        elif choice == '4':
            
            insect.print_intro()
            animal = 'insect'
            animal_set = insect_set
            return [animal, animal_set, True]
            break
            
        elif choice == '5':
            
            print('Exiting. Thanks for visiting!')
            return [None, None, False]
            break
            
        else: 
            
            print('Invalid selection. Enter any new key to continue: ')
                       
            
#secondary menu once animal category is chosen
def category_menu(animal, animal_set):
    
    """Prints the secondary menu and returns the number for the specific animal chosen so that instance can be indexed."""
    
    print_category_menu(animal, animal_set)
    animal_number = input()
    animal_number = remove_punctuation(animal_number)
    
    return animal_number


#specific secondary menu function which takes in the list of animals for the respective category
def print_category_menu(animal, animal_set):
    
    """General function to print secondary menu which takes in the animal list returned in menu_choice"""
    
    print('Which specific ' + animal + ' would you like learn about?\n')
    
    counter = 1
    
    for each in animal_set:
                 
        counter  = str(counter)
        print(counter + ". " + each.name)
        counter = int(counter) + 1
        
