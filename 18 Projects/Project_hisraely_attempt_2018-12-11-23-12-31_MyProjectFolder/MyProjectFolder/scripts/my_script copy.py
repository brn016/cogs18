import random
import string

def pick_word():
  """
  This function picks a random word from a list of words.
  """
  pick = random.choice(words)
  pick = list(pick)
  return pick

def check_win():
  """
  Check if user won the game.
  """
  if '_' in guess:
    return False

  return True




playing = True

words = ['guitar','piano','duduk','clarinet','saxophone','violin','drums', 'trombone']



while playing:
  word = pick_word()
  guess = ['_' for _ in word]
  tries = 10

  print("\n\nWelcome to hangman. Good luck :)")

  alphabet = list(string.ascii_lowercase)
  while True:
    print("\nTry to guess a letter. You have " + str(tries) + " tries remaining.")
    print(guess)

    valid_guess = True
    while valid_guess:
      letter = input()
      if letter in alphabet:
        valid_guess = False
      else:
        print("You already picked that letter! Try to guess another letter.")


    guessed_correct = False 
    for idx, val in enumerate(word):
      if letter == val:
        guess[idx] = letter
        guessed_correct = True

    if guessed_correct:
      print("Nice guess!")
    else:
      print("No matches, try again :(")
    tries += -1
    alphabet.remove(letter)

    if check_win():
      print("You win! Congratulations!!!!")
      break
   
    if tries == 0:
      print("You lose :( Better luck next time!")
      break


  play_again = input("\nWould you like to play again (Y/N)")
 
  if play_again == 'Y' or play_again == 'y':
    pass
  else:
    playing = False

  
