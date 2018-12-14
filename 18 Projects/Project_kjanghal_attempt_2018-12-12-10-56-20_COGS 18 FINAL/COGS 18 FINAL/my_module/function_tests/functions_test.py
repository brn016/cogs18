yes_list = ["yes", "Yes", "yeah", "Yeah", "yea", "Yea", "yup", "Yup", 
            "aye", "Aye", "affirmative", "Affirmative", "y", "Y", "1", "True"]
no_list = ["no", "No", "nope", "Nope", "nah", "Nah", "nay", "Nay", "negative", 
           "Negative", "n", "N", "0", "False"]
high_sev = ["11", "12", "13", "14"]
med_sev = ["8","9","10"]
low_sev = ["0", "1", "2", "3", "4", "5", "6", "7"]

from my_module/functions.py import yes_or_no, true_symptoms

def test_yes_or_no:
    input_msg = "affirmative"
    answer = yes_or_no(input_msg)
    
    assert answer == 'yes'