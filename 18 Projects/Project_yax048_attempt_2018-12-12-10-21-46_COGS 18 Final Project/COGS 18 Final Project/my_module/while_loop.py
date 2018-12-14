def while_loop_answer():
    """Keep reporting error if the answer is not valid"""
    
    msg = input('INPUT :\t')
    # Check if user's answer is valid(Yes or No)
    if msg == 'No':
        print('Thank you and have a great day!')
        chat = False
    elif msg == 'Yes':
        print('Okay, give me a second...')
        chat = True
        
    # If answer is not valid, start a while loop
    else:
        while msg != 'Yes' or 'No':
            
            # Keep reporting error if the answer is not valid
            print("Sorry, I can't understand you. please call (888)888-8888")
            print('Anything else I can help you with? (please answer Yes or No)')

            msg = input('INPUT :\t')
            
            # When answer is No, break this while loop and return chat=False which will end the chatbot loop.
            if msg == 'No':
                print('Thank you and have a great day!')
                chat = False
                break
            
            # When answer is Yes, break this while loop and return chat=True which will keep the chatbot loop.
            elif msg == 'Yes':

                print('Okay, give me a second...')
                chat = True
                break
            
    return chat