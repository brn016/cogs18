#there are 11 different "pictures" in hangman, one prints after each wrong guess
#hangman pictures found in: https://codereview.stackexchange.com/questions/95997/simple-game-of-hangman
hangman = [
"""
-----
|   |
|
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|  -+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  |
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | 
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | | 
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | | 
|  | | 
|
--------
"""]


#for the random words run: pip install RandomWords (find the documentation here: https://pypi.org/project/RandomWords/0.1.5/)
from random_words import RandomWords
rw = RandomWords()



def new_word():
    '''This function chooses a random word for the game from the downloaded RandomWords package.'''
    return list(rw.random_word())


def update_state(player_guess, current_state, game_word):
    '''This function looks through the letter that the player guesses and assesses if it's in the game word
    then adds the letter to the current state of the word, creating a new state'''
    #initializes a new variable to represent the new state of the game word once player starts guessing letters
    new_state = []
    
    #checks if the player's guess is in "n" position in the game word and
    #updates the new state of the game word to contain the guessed letter at position "n"
    for n in range(0, len(game_word)):      
        if player_guess == game_word[n]:
            new_state += player_guess
        else:
            new_state += current_state[n]
    
    #returns what the game word looks like now that the guess letter has been put into its space 
    #OR returns the same state as before if the guess letter was not in the game word
    return new_state
            

def main():
    
    #calls function new_word to generate a random new word for each game
    game_word = new_word()
    
    #initializes a list of letters that have already been guessed
    guessed_letters = []
    
    #this section initializes the current state to be a number of blank spaces equal to the number of letters in the game word
    current_state = []
    
    #this displays an empty space in the form of an underscore for each letter in the game word
    for char in game_word:
        current_state += ["_"]
    
    #this prints out a space between each underscore for each letter of the game word
    #so that they player can actually see how many letters there are, not just a straight line of underscores
    print(" ".join(current_state))

    #the number of guesses the player can make should be the maximum number of hangman "pictures" there are 
    #since when the picture is complete, the player has no more guesses and loses 
    number_of_guesses = len(hangman) - 1
    
    while number_of_guesses > 0:
        #we want to show to the user how many guesses they have left
        print("You have " + str(number_of_guesses) + " guesses left")  
        
        #this asks the player to guess a letter
        player_guess = input("Next letter:")
        
        #this checks if what the player guessed is a letter,
        #also checks if it is just 1 letter
        #also checks if the letter has been previously guessed
        if player_guess.isalpha() and len(player_guess) == 1 and player_guess not in guessed_letters:
            #adds all new guesses to the list of guessed letters, so that they can't be guessed again
            guessed_letters += [player_guess]
            #we call on the update_state function with the inputs player_guess and current_state
            new_state = update_state(player_guess, current_state, game_word)
                
            #checking if the new state of the word has not changed because of a wrong guess
            #subtracts 1 wrong guess from total number of wrong guesses left 
            if new_state == current_state:
                number_of_guesses -= 1
                print("Sorry, this letter is not in the word")
                
            #updates the current state of the guessed word to inlude a mix of underscores and correctly guessed letters    
            current_state = new_state
            
            print(" ".join(current_state))
            
            #prints out the hangman picture corresponding to the number of guesses left
            #adds one body part for each wrong guess
            print(hangman[len(hangman) - number_of_guesses - 1])
            
            #checks if the game word has been fully guessed, and prints out a "you won" statement if it has
            if current_state == game_word:
                print("Congratulations, you won!!!")
                break
         
        else:
            #if the guess isn't 1 non-previously guessed letter, we tell the user their guess is invalid
            print("Sorry, this is an invalid guess")
        
        #if the person has used up all their guesses and the hangman is complete, they lose
        if number_of_guesses == 0:
            print("Sorry, you lost. The word was " + "".join(game_word))

            

#this is the actual code that runs
#just a welcome message         
print("Welcome to my Hangman Game.")

#calls on the main function to execute the Hangman game
main()

#this while loop finishes the game up by asking if the player wants to play again
while True:

    play_again = input("Do you want to play again? If yes, press Y. If no, press N")

    #if the player wants to play again and answers yes, the main function runs again and the game restarts with a new word
    if play_again == "Y":
        main()
        
    #if the player answers no to playing again, the game ends 
    else:
        print("thanks for playing, goodbye!")
        break