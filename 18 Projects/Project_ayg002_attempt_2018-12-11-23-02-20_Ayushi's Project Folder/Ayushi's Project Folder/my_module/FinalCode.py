# A Game of Cyphers! 

import random
class Game():
    
    
    dictionary_of_keys = {
            '1' : ['100-99' , '10-9' , '1022-1023+2'],
            '2' : ['102%50' , '1+3-2' , '222/111'],
            '3' : ['99-96' , '300/100' , '768%255'],
            '4' : ['1+1+1+3-2' , '2*2' , '24%5'],
            '5' : ['2*2+1' , '25/5' , '155%30']
        }
    
    # Initializer, which allows us to specificy instance specific attributes
    def __init__(self):
        self.user1_score = 0
        self.user2_score = 0
        
        
    def instructions(self):
        print("""Instructions
              1. User 1 enters a message of 5 words of less (n<=5).
              2. User 2 sees an encrypted message and is presented with n math problems.
              3. Answers to the n math problems are cyphers that will help decode the encrypted message.
              4. User 2 now has two tries to arrange the n cyphers in the correct order.
              5. If User 2 cannot get the order right in two tries, the round ends and User 1 gets 1 point, 
                  User 2 gets 0.
              6. After round 1, User 2 enters a message and User 1 decrypts the message.
              7. Their score is added to a running total. The game ends after 5 rounds and the User with 
                  the highest score wins the game.
        """)
        
    #grabs input from user and checks if it is valid
    def user1_input(self):
        print("Enter a message of less than 5 words: ")
        
        user1_s = input('INPUT :\t')

        while len(user1_s.split()) > 5:
            user1_s = input('Please enter a message less than 5 words without any characters. :\t')
        
        return user1_s 
    
    # add a test for message to be less than 5 words
    # encodes message and asigns values to keylist
    def encoding_message(self, user1_s, keylist):
        
        encoded = "" 
        user1_words = user1_s.split(" ")
        
        index = 0
        for item in user1_words:
            key = keylist[index]
            for char in item:
                encoded += chr(ord(char) + key)
            encoded += " "
            index += 1
        #removes the extra space at the end
        encoded = encoded[:-1]
        self.keylist = keylist
        
        return encoded
    
    #takes a keylist that was used to encrytp and returns a shuffled copy of it
    def shuffled_cypher_questions(self, keylist):
        user2_keylist = []
        keylist_1 = keylist[:]
        random.shuffle(keylist_1)
        return keylist_1
    
    def record_user_input_to_questions(self, shuffled_key_list):
        user2_keylist = []
        for item in shuffled_key_list:
            QuestionList = self.dictionary_of_keys[str(item)] #find a corresponding dictionary item == key
            print('Solve this: ' + random.choice(QuestionList))
            
            user2s_1 = input('Enter your answers to the above problems. Enter the answers without spaces. :\t')
            
            while user2s_1.isdigit() == False and user2s_1.contains(" "):
                user2s_1 = input('Enter your answers to the above problems. Enter ONLY numbers, without spaces please. :\t')
            user2_keylist.append(user2s_1)
            print('\n')
        return user2_keylist
    
    def instructions_2(self):
        print('Try to decrypt the above message.')
        print('To do so, look over your answer to the above problems and find the correct order of cyphers.')
        
        
    # user 2 now has 2 tries to get the correct order
    # userTwoAnswer holds the answer for user two in a string
    # correct answer is what we expect the answer to be in list format
    # last try is a boolean to see if this is user two's last attempt
    # returns a true if the answer matches and false otherwise
    def check_answer(self, usertwo_answer, correct_answers, last_try):
        correct_answer = str()

        for item in correct_answers:
            correct_answer += str(item)
        
        if usertwo_answer == correct_answer:
            print('You win!')
            self.user2_score += 1
            return True
    
        elif(lastTry):
            print('You lose. Haha.' + '\n')
            self.user1_score += 1
            
        else:
            print('Wrong answer. Try again:')
            
        return False
    
    def get_usertwo_answer(self):
        return input('Player 2 input :\t')
        
    def print_scores(self):
        print('Scores: ' + 'User 1 = '+ str(self.user1_score) +', ' + 'User 2 = ' + str(self.user2_score) + " ." + '\n' + '\n')
    
    def startGame(self):
        self.instructions()
        i = 0
        while i < 3:
            message = game.user1_input()
            key_list = []

            # generate ranodm keys for each word 
            for word in message.split():
                key_list.append(random.randint(1,5))

            # encode message using random keys
            encoded = game.encoding_message(message, key_list)
            print('ENCODED MESSAGE : ' + encoded + '\n')

            # shuffle the keys we used to encrypt 
            shuffled_key_list = game.shuffled_cypher_questions(key_list)

            # get user two's responses
            responses = game.record_user_input_to_questions(shuffled_key_list)
            
            # give user 2 their instructions
            game.instructions_2()
            
            usertwo_guess = game.get_usertwo_answer()
            # check if the user gave the incorrect answer
            if(not(game.check_answer(usertwo_guess, key_list, False))):
                usertwo_guess = game.get_usertwo_answer()
                game.check_answer(usertwo_guess, key_list, True)
            game.print_scores()
            i += 1

        print('GAME OVER!')

