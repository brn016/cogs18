def end_chat(input_msg):
    """Checks to see if the input message contains a quirt response.
    
    TAKEN FROM ASSIGNMENT 3 (CHATBOX)
   
    Parameters
    ---------
    input_msg : string
       string that will be analyzed for 'quit' response
       
    Returns
    -------
    output: boolean
        boolean determining whether to quit the chat
    """
    if 'quit' in input_msg:
        output = True
    else:
        output = False
    return output

def yes_or_no (input_msg):
    """Checks to see if the input message contains a yes or no response.
    
    Parameters
    ---------
    input_msg : string
       string that will be analyzed for 'yes' or 'no' response
       
    Returns
    -------
    answer: string
        string containing the interpretation of the user's response
    """
    if input_msg in yes_list:
        answer = "yes"
    elif input_msg in no_list:
        answer = "no"
    elif input_msg not in yes_list and input_msg not in no_list:
        answer = "unknown"
    return answer
def days_check(input_msg):
    """Categorizes the number of days into severity levels.
    
    Parameters
    ---------
    input_msg : string
       string that will be analyzed for numerical response
       
    Returns
    -------
    severity: string
        string containing high, medium, or insignificant interpretation of the user's response
    """
    if input_msg in high_sev:
        severity = "high"            
    elif input_msg in med_sev:
        severity = "medium"
    elif input_msg in low_sev:
        severity = "insignificant"
    else:
        severity = "unknown"
    return severity

def true_symptoms(symptom_list):
    """Totals the number of symptoms that have been indicated to be present by the user.
    
    Parameters
    ---------
    symptom_list : list
       list of all the symptoms that the user was asked to respond to
       
    Returns
    -------
    true_symptoms: integer
        integer of the total number of present symptoms as indicated by the user
    """
    true_symptoms = 0
    for symptom in symptom_list:
        if symptom.presence == True:
            true_symptoms = true_symptoms + 1
    return true_symptoms

def high_sev_count(symptom_list):
    """Totals the number of symptoms that have been categorized as "high" severity.
    
    Parameters
    ---------
    symptom_list : list
       list of all the symptoms that the user was asked to respond to
       
    Returns
    -------
    high_symptoms: integer
        integer of the total number of "high" severity symptoms as indicated by the user
    """
    high_symptoms = 0
    for symptom in symptom_list:
        if symptom.severity == "high":
            high_symptoms = high_symptoms + 1
    return high_symptoms

def med_sev_count(symptom_list):
    """Totals the number of symptoms that have been categorized as "medium" severity.
    
    Parameters
    ---------
    symptom_list : list
       list of all the symptoms that the user was asked to respond to
       
    Returns
    -------
    med_symptoms: integer
        integer of the total number of "medium" severity symptoms as indicated by the user
    """
    med_symptoms = 0
    for symptom in symptom_list:
        if symptom.severity == "medium":
            med_symptoms  = med_symptoms + 1
        return med_symptoms