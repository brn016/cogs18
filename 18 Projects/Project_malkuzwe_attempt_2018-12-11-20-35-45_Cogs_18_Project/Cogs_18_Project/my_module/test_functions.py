
from functions import separate, remove_last_chara, remove_first_chara
import pandas as pd

data_1 = [['A.', 1], ['B.', 2], ['C.', 3]]
df_1 = pd.DataFrame(data_1, columns=['Col1', 'Col2'])


data_2 = [['.A', 1], ['.B', 2], ['.C', 3]]
df_2 = pd.DataFrame(data_1, columns=['Col1', 'Col2'])


data_3 = [['A.B', 1], ['C.D', 2], ['E.F', 3]]
df_3 = pd.DataFrame(data_3, columns=['Col1', 'Col2'])


def test_remove_last_chara():
    
    """Test for remove_last_chara function"""
    
    assert isinstance(remove_last_chara(df_1, 'Col1'), pd.DataFrame)
    
    
def test_remove_first_chara():
    
    """Test for remove_first_chara function"""
    
    assert isinstance(remove_first_chara(df_2, 'Col1'), pd.DataFrame)
    
    
def test_separate():
    
    """Test for separate function"""
    
    assert isinstance(separate(df_3, 'first', 'second', 'Col1', '.'), pd.DataFrame)