"""A collection of function for doing my project."""
def is_question(input_string):
    
    if '?' in input_string:
        output = True
    else:
        output = False
    
    return output

def remove_punctuation(input_string):
    
    out_string = ''
    for char in input_string:
        if char not in string.punctuation:
            out_string += char
            
    return out_string

def prepare_text(input_string):
    
    temp_string = input_string.lower()
    temp_string = remove_punctuation(temp_string)
    out_list = temp_string.split()
    
    return out_list

def respond_echo(input_string, number_of_echoes, spacer):
    
    if input_string is not None:
        echo_output = (input_string+spacer)*(number_of_echoes)
    else:
        echo_output = None
    
    return echo_output 

def selector(input_list, check_list, return_list):

    output = None
    for word in input_list:
        if word in check_list:
            output = random.choice(return_list)
            break

    return output

def string_concatenator(string1, string2, separator):
    
    result = string1 + separator + string2
    
    return result

def list_to_string(input_list, separator):
    
    output = input_list[0]
    for item in input_list[1:]:
        output = string_concatenator(output, item, separator)
        
    return output

def end_chat(input_list):
    
    if 'quit' in input_list:
        output = True
    else:
        output = False
        
    return output

def is_in_list(list_one, list_two):
    """Check if any element of list_one is in list_two."""
    
    for element in list_one:
        if element in list_two:
            return True
    return False

def find_in_list(list_one, list_two):
    """Find and return an element from list_one that is in list_two, or None otherwise."""
    
    for element in list_one:
        if element in list_two:
            return element
    return None


def have_a_chat():
    """Main function to run our chatbot."""
    
    chat = True
    while chat:

        # Get a message from the user
        msg = input('How are you? :\t')
        out_msg = None

        # Check if the input is a question
        question = is_question(msg)

        # Prepare the input message
        msg = prepare_text(msg)

        # Check for an end msg 
        if end_chat(msg):
            out_msg = 'Bye, Have a great New Years! c:'
            chat = False

        # Check for a selection of topics that we have defined to respond to
        #   Here, we will check for a series of topics that we have designed to answer to
        if not out_msg:

            # Initialize to collect a list of possible outputs
            outs = []

            # Check if the input looks like a greeting, add a greeting output if so
            outs.append(selector(msg, GREETINGS_IN, GREETINGS_OUT))

            # Check if the input looks like a computer thing, add a computer output if so
            outs.append(selector(msg, COMP_IN, COMP_OUT))
            
            #added mood***
            outs.append(selector(msg, REFLECTION_IN, REFLECTION_OUT))
            #added mood***
            outs.append(selector(msg, POS_IN ,POS_OUT))
            
            # Check if the input mentions a person that is specified, add a person output if so
            if is_in_list(msg, PEOPLE_IN):
                name = find_in_list(msg, PEOPLE_IN)
                outs.append(list_to_string([PEOPLE_NAMES[name], name.capitalize(),
                                            selector(msg, PEOPLE_IN, PEOPLE_OUT)], ' '))

            # Check if the input looks like a joke, add a repeat joke output if so
            outs.append(respond_echo(selector(msg, JOKES_IN, JOKES_OUT), 3, ''))
           
            #pic emoji name correspondece/added ***
            if is_in_list(msg, EMOJI_IN):
                emoji = find_in_list(msg, EMOJI_IN)
                outs.append(list_to_string([EMOJI_NAME[emoji], selector(msg, EMOJI_IN, EMOJI_OUT)], ' '))


            # Check if the input has some words we don't want to talk about, say that, if so
            if is_in_list(msg, NONO_IN):
                outs.append(list_to_string([selector(msg, NONO_IN, NONO_OUT), find_in_list(msg, NONO_IN)], ' '))

        
            options = list(filter(None, outs))
            if options:
                out_msg = random.choice(options)

        # If we don't have an output yet, but the input was a question, return msg related to it being a question
        if not out_msg and question:
            out_msg = QUESTION

        # Catch-all to say something if msg not caught & processed so far
        if not out_msg:
            out_msg = random.choice(UNKNOWN)

        print('OUTPUT:', out_msg)
        
        
  

