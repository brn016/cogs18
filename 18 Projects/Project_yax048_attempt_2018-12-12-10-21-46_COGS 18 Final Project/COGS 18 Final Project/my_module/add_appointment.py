# Define a function to print out messages one by one
def question1():
    """The first question bot ask user"""
    # Create a tuple of the messages for question 1
    question_1 = (("Hi! Welcome to Tyler's Repair shop."),
    ('What can I help you with? (please chose 1, 2, or 3)'),
    ('1. Make an appointment'),
    ('2. Check your appointment'),
    ('3. Cancel your appointment'))
    for i in question_1:
        print(i)

# Define a function to print out messages one by one 
def question11():
    """The second question bot ask user"""
    #Create a tuple of the messages for the second question when user give answer "1" in question 1.
    question_1_1 = (('What kind of service do you need?(please chose 1, 2, or 3)'),
    ('1. Tire replacement'),
    ('2. Bumper replacement'),
    ('3. Light replacement'))
    for i in question_1_1:
        print(i)

# Write a funtion to make different appointments use add_appointment method of the class reservation_list
def add_appoint():
    """add appointment for user with method created"""
    from my_module.reservation import reservation_list as p
    from my_module.reservation import remove_key
    r = p()
    # Define the third question after user choose the answers from second question
    question_1_1_1 = ('Please enter the appointment time you want to make (please choose the number)')
    # Ask the second question
    question11()
    # Let user answer the question
    msg1_1 = input('INPUT :\t')
    
    # If the answer is '1', show user the avaliable times
    if msg1_1 == '1':
        print(question_1_1_1)
        r.check_avaliable()
        # Add an appointment using add_appointment method with job name 'Tire replacement'
        msg1_1_1 = input('INPUT :\t')
        r.add_appointment('Tire replacement', msg1_1_1)
        
    # If the answer is '2', show user the avaliable times  
    elif msg1_1 == '2':
        print(question_1_1_1)
        r.check_avaliable()
        # Add an appointment using add_appointment method with job name 'Bumper replacement'
        msg1_1_2 = input('INPUT :\t')
        r.add_appointment('Bumper replacement', msg1_1_2)
        
    # If the answer is '3', show user the avaliable times
    elif msg1_1 == '3':
        print(question_1_1_1)
        r.check_avaliable()
        #Add an appointment using add_appointment method with job name 'Light replacement'                    
        msg1_1_3 = input('INPUT :\t')
        r.add_appointment('Light replacement', msg1_1_3)      
    
    # If the answer is unvalid, report error.
    else:
        print("Sorry, I can't understand you. please call (888)888-8888")