import time

#initialize an empty list that we will append in the future
cowboy_goodies = [] 

#create a function to easily repeat this elaborate conditional whenever necessary
def direction_prompt(direction): 
    """
    execute a conditional based on string inputs
    
    parameters: direction = string
    """
    if direction == "saloon": 
        cowboy_goodies.append("Fancy Hat") #add a string to the running list of items
        print("You Have:", cowboy_goodies)
        print("Congrats, you have picked up a real nice Hat!") 
    elif direction == "wilderness":
        cowboy_goodies.append("Shiny Badge")
        print("You Have:", cowboy_goodies)
        print("Congrats, you have picked up a Badge!")
    else:
        direction = input("Saloon or Wilderness?") #the input method prompts user to answer printed question again
        direction_prompt(direction) #if desired input is not achieved under if/elif statements, we can just run the entire function again
        direction = direction.lower() #this creates a uniform input in case users capitalize inputs 
        
#create another function to easily repeat an elaborate conditional whenever necessary        
def frontier_prompt(yes_or_no, cowboy_goodies): 
    """
    execute a conditional based on string inputs
    
    parameters: yes_or_no = string, cowboy_goodies = list
    """
    if yes_or_no == "yes":
        print("Congrats, you found a single cowboy boot!")
        cowboy_goodies.append("Boot")  #add another string to the running list of items
        print("You Have:", cowboy_goodies)
        time.sleep(3)
        print(" ")
        print("You proceed into the Frontier.")
        print("A shadowy figure appears.")
        print("Would you like to go up to this shadowy figure? Or run away?")
        cowboy = input("Enter 'go up to him' or 'run away'" + " ") 
        cowboy = cowboy.lower()  
        cowboy_prompt(cowboy) #run another defined function, only if previous input executed the if statement
    elif yes_or_no == "no":
            print(" ")
            print("You are a coward.")
            cowboy_goodies = [] #the list of items is emptied because the input executed the elif statement
            print("Sheriff arrests you for cowardly behavior and takes all your goodies.")
            print("You're lucky he ain't gonna hang you, pardner.")
            print("You Have:", cowboy_goodies)
    else:
            yes_or_no = input("Yes or No?" + " ") #input re-prompted
            frontier_prompt(yes_or_no, cowboy_goodies) #function re-executed
            yes_or_no = yes_or_no.lower() #uniformity of input

#create another function to repeat this conditional whenever necessary
def cowboy_prompt(cowboy):
    """
    execute a conditional based on string inputs
    
    parameters: cowboy = string, cowboy_goodies = list
    """
    if cowboy == 'go up to him':
        print("Mr. Shadowy figure turns out to be just a sweet, lonely cowboy looking for a friend.")
        print("Howdy, new best friend!")
        time.sleep(1)
        print(" ")
        print("Congrats, Mr. Cowboy gave you some Pointy Boys and a western whistling tube!")
        [cowboy_goodies.append("Spurs"), cowboy_goodies.append("Harmonica")] #this if pathway appends two strings to the list
        print("You Have:", cowboy_goodies) 
    elif cowboy == 'run away':
        cowboy_goodies.remove("Boot") #lose something out of your list because you got 'robbed' (this is a string definitely in your list already from executing the if statement in the previous function (frontier_prompt))
        print(" ")
        print("He saw you.")
        print("He's pulling out his gun.")
        time.sleep(3)
        print(" ")
        print("oh my god you have skullcandy™ earbuds in") #this story follows a scenario in which you don't know you're in a shootout
        print("you can't hear him")
        time.sleep(1)
        print(" ")
        print("oh my god")
        time.sleep(1)
        print(" ")
        print("He shoots you and takes your single boot.")
        time.sleep(1)
        print(" ")
        print("'THERE'S ME OTHER SHOE!!!' he cackles")
        print("You Have:", cowboy_goodies) 
    else:
        cowboy = input("Enter 'go up to him' or 'run away'" + " ") #input method is prompted again
        cowboy_prompt(cowboy) #if the input doesn't execute desired if/elif conditions, function is executed again
        cowboy = cowboy.lower() #uniformity of answers
        
#create another function to repeat conditional when needed
#create a certain number of acceptable inputs that will execute part of the conditional statement
def drink_prompt(drink, cowboy_goodies):
    """
    execute a conditional based on string inputs
    
    parameters: drink = string, cowboy_goodies = list
    """
    if drink == 'water':
        print("Refreshing choice.")
        print("It's good to stay hydrated.")
        cowboy_goodies.append("High Five") #each if/elif appends a different string into the list
        print("You get a high five from the bartender.")
        print("You Have:", cowboy_goodies)
    elif drink == 'beer':
        print("hmmmmmmmmmmmmmmmmmmmm")
        cowboy_goodies.append("Questionable Glance")
        print("The bartender gives you a look.")
        print("You Have:", cowboy_goodies)
    elif drink == 'whiskey':
        print("What a Manly COwboy Drink That Is!")
        print("You must be Tough As Nails!")
        cowboy_goodies.append("Affirming Nod")
        print("The bartender gives you an affirming nod.")
        print("You Have:", cowboy_goodies)
    elif drink == 'scotch':
        print("Ah. Also a Fella of Class, I See!")
        cowboy_goodies.append("Free Drink")
        print("You Have:", cowboy_goodies)
        print("The bartender offers you another round on the house!")
    elif drink == 'milk':
        print("Hmmmm?")
        time.sleep(1)
        print("Huh?")
        time.sleep(3)
        print("Hey, fella, are you okay there?")
        cowboy_goodies.append("Concern.")
        print("You Have:", cowboy_goodies)
    else: #if the input does not execute if/elifs, prompt the user to choose another option
        print("I'm sorry, they don't serve that here.") #politely let the customer down
        drink = input("What will you have?" + " ") 
        drink_prompt(drink, cowboy_goodies) 
        drink = drink.lower()