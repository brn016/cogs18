def remember_punc(str1):
    """Stores punctuations at end of strings.
    
    Parameters
    ----------
    str1 : str
        The string with possible punctuation at end.
        
   
    Returns
    ------
    last_char : str
        The last punctuation in the string or a blank string.
    
    
    """
    punctuation = ['.', ',', '#', '!', '?', '~', ':','%']
    last_char = str1[-1]
    if last_char in punctuation:
        return last_char
    else:
        last_char = ''
        return last_char
    
    
    
def choose_num(lower_bound, upper_bound):
    """Randomly chooses a number within given bounds. Returns integer as a string.
    
    Parameters
    ----------
    lower_bound : int
        The lower boundary of numbers to select from. 
    upper_bound : int
        The upper boundary of numbers to select from. 
        
    Returns
    -------  
    string_integer : str
        The randomly chosen number as a string. 
    
    """
    import random
    integer = random.choice(range(lower_bound,upper_bound))
    string_integer = str(integer)
    return(string_integer)



def replace_words (str1, genre):
    """Replaces indicated words with a randomly selected number word in a list from genre dictionary. 
    
    Parameters
    ----------
    str1 : str
        The string containing indicated words to replace.
    genre : dict
        The dictionary containing lists of words that will replace string words.
    
    Returns
    -------
    str1 : str
        The string with the indicated words replaced. 
    
    """
    
    import random

#split string into list of words 
#use remember_punc to keep punctuations in strings
    
    list1 = str1.split()
    for item in list1:
        if '/plural_noun' in item:
            punc = remember_punc(item)
            str1 = str1.replace(item, random.choice (genre['plural_noun'])+ punc)
        
        if '/noun' in item :
            punc = remember_punc(item)
            str1 = str1.replace(item, random.choice(genre['noun']) + punc)        
        
        if '/adjective' in item:
            punc = remember_punc(item)
            str1 = str1.replace (item, random.choice(genre['adjective']) + punc)
        
        if '/name' in item:
            punc = remember_punc(item)
            str1 = str1.replace(item, random.choice(genre['name'])+ punc)
        
        if '/past_verb' in item:
            punc = remember_punc(item)
            str1 = str1.replace(item, random.choice(genre['past_verb'])+ punc)
        
        if '/verb' in item:
            punc = remember_punc(item)
            str1 = str1.replace(item, random.choice(genre['verb'])+ punc)
        
        if '/adverb' in item:
            punc = remember_punc(item)
            str1 = str1.replace(item, random.choice(genre['adverb'])+ punc)
        
        if '/location' in item:
            punc = remember_punc(item)
            str1 = str1.replace(item,random.choice(genre['location'])+ punc)
        
        if '/number' in item:
            punc = remember_punc(item)
            str1 = str1.replace(item, choose_num(-100,100) + punc)
    
    return str1



def remember_ends(str1):
    """Stores the last punctuation of the string
    
    Parameters:
    -----------
    str1 : str
        The string the last punctuation is derived from.
        
    Returns:
    -------
    punc : str
        The last punctuation in a string or a blank string.
    
    """
#modified remember_punc to keep punctuation at ends of string
 
    pun = ['.', '!', '?']
    last_char = str1[-1]
    if last_char in pun:
        punc = last_char
    else:
        punc = ''
    return punc




def remove_ends(str1):
    """Removes the last punctuation of the string.
    
    Parameters:
    -----------
    str1 : str
        The string the last punctuation is removed from.
    
    Returns:
    --------
    str1 : str
        The string with punctuation at the end removed.
    
    """
    pun = ['.', '!', '?']
    last_char = str1[-1]
    if last_char in pun:
        str1 = str1[0:-1]
    return str1



def cap_sentences (punctuation, sentences):
    """Fixes capitalization for characters following an indicated punctuation.
    Parameters:
    -----------
    punctuation : str
        The punctuation preceding the words to be capitalized.
    sentences : str
        The string of sentences.
        
    Returns:
    --------
    capitalized_sentences : str
        The string of sentences with the character(s) following indicated punctuation capitalized.
        
    """
    
    split_sentences = sentences.split(punctuation)
    final_strings=[]
 
 #.strip to avoid capitalizing empty spaces
    for string in split_sentences:
            
            string = string.strip()
            new_string = string[0].upper() + string[1:]
            final_strings.append(new_string)
            insert = punctuation + ' '
            capitalized_sentences = insert.join(final_strings)
    
    return capitalized_sentences


def fix_all_caps(sentences):
    """Fixes capitalization for strings containing the normal sentence endings "!", "?", and ".".
    Parameters:
    ----------
    sentences : str
        A string of sentences.
    
    Returns:
    -------
    fixed_sentences : str
        A string of sentences with the first character of every sentence capitalized.

    """
#store last punctuation in string as punc
#removes last punctuation of string
    
    punc = remember_ends(sentences)
    sentences = remove_ends(sentences)

#split strings and capitalizes first char following ".", "!", and "?"

    if '.' in sentences:
        sentences = cap_sentences('.', sentences)
    
    if '!' in sentences:
        sentences = cap_sentences('!', sentences)
    
    if '?' in sentences:
        sentences = cap_sentences('?', sentences)
    
    fixed_sentences = sentences + punc
    
    return(fixed_sentences)


def madlib(madlib, genre):
    """A function to fill in madlibs.
    
    Parameters:
    -----------
    madlib : str
        The madlib with words to be replaced.
    
    genre : dict
        A dictionary containing lists of words to fill into madlib.
        
    Returns:
    --------
    filled_and_fixed : str
        The madlib with words filled in and capitalization fixed.
    
    """
    filled = replace_words(madlib, genre)
    filled_and_fixed = fix_all_caps(filled)
    return filled_and_fixed

