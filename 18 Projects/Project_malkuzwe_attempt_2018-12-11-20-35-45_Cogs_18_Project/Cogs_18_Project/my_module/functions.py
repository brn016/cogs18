

def remove_last_chara(df, column_name):
    """Removes the last character of each element in a column in a dataframe.
    
    Parameters
    ----------
    df : Pandas dataframe
        Dataframe that contains the column we will be indexing through
    
    column_name : string
        The name of the column we will be indexing through
       
    Returns
    -------
    df : Pandas dataframe
        Dataframe that now contains the updated column
    """
        
    df[column_name] = df[column_name].map(lambda x: str(x)[:-1])
  
    return df


def remove_first_chara(df, column_name):
    """Removes the first character of each element in a column in a dataframe.
    
    Parameters
    ----------
    df : Pandas dataframe
        Dataframe that contains the column we will be indexing through
    
    column_name : string
        The name of the column we will be indexing through
       
    Returns
    -------
    df : Pandas dataframe
        Dataframe that now contains the updated column
    """
    
    df[column_name] = df[column_name].map(lambda x: str(x)[1:])
    
    return df

           
def separate(df, column_name_1, column_name_2, old_column, character):
    """Separates each value in a column along a certain character and creates two new columns
    
    Parameters
    ----------
    df : Pandas dataframe
        Dataframe that contains the column we will be indexing through
        
    column_name_1 : string
        The name of the first new column we will create by separating the original column
        
    column_name_2 : string
        The name of the second new column we will create by separating the original column
        
    old_column : string
        The name of the original column that we will separate along a certain character into two new columns
        
    character : string
        The character contained in each value of the old_column that we will separate the value at
    
    Returns
    -------
    df : Pandas dataframe
        Dataframe that contains the two new updated columns (in addition the old column that we can ignore)
    """
        
    df[column_name_1], df[column_name_2] = df[old_column].str.split(character, 1).str
    
    return df
   