"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

from functions import calculate_grades

##
##

def calculate_grades():
    
    test_student = Student(1,2,3,4)
    total_grade = calculate_grade(test_student)
    
    assert total_grade == 4

    
    