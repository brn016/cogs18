import sys
sys.path.append('./')

from my_module.functions import color_cholesterol_level, color_blood_pressure
        
    
def test_correct_colors():
   
    """
    test_correct_colors()
    
    A function that tests whether the functions color_cholesterol_level and color_blood_pressure return the correct color when an input is parsed in. 
    """
    
    assert color_cholesterol_level(190) == 'color: black'
    assert color_cholesterol_level(200) == 'color: orange'
    assert color_cholesterol_level(240) == 'color: red'
    
    assert color_blood_pressure(119) == 'color: black'
    assert color_blood_pressure(120) == 'color: orange'
    assert color_blood_pressure(130) == 'color: red'
