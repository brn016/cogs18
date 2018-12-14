def is_question(input_string):

    output = bool

    if '?' in input_string:
        output = True
    else:
        output = False
    return output

def is_msg_question(input_string):
    list_1 = input_string.split()
    if 'question' in list_1:
        return True
    elif 'ask' in list_1:
        return True
    else:
        return False

def remove_punctuation(input_string):
    out_string = ''
        for character in input_string:
            if character not in string.punctuation:
                out_string += character
            else:
                pass
        return out_string

def list_to_string(input_list, separator):
    output = input_list[0]

    for item in input_list[1:]:
        output = string_concatenator(output, item, separator)

    return output

def prepare_text(input_string):

    input_string = input_string.lower()

    input_string = remove_punctuation(input_string)

    out_list = input_string.split()

    return out_list

def selector(return_list):
    output = None
    output = random.choice(return_list)

    return output

def end_chat(input_string):
    input_string = input_string.lower()

    input_string = remove_punctuation(input_string)

    output_list = input_string.split()

    if 'quit' in output_list:
        output = True
    else:
        output = False
    return output
