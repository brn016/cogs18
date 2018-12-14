
from functions import execute_action
from objects import Chair

def test_execute_action():
    
    test_string = "Kick the table"
    test_thing = None
    
    test_output = execute_action(test_thing, test_string)
    
    if test_output == "Try another object in the room.":
        return True
    else:
        return False
   