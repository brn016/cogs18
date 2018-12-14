import pandas as pd
import collections

def new_hof(lst_1,lst_2):
    
    """Cross examine both lists to find pitchers that appears in both lists and creates new list with names of those pitchers.
    
    Parameters
    ----------
    lst_1: list of hall of fame players
    lst_2: list of hall of fame pitchers
    
    Returns
    -------
    new_hof: list
    
    The result of names that appear in both lists
    
    """
    
    
    #initialize a set for both pitchers list and hof list
    n_hof = set()
    n_pitch = set()

    # for loop will go into every item in the specified column of the dataframe to append to the intialized sets
    for item in lst_1:
    
        n_hof.add(item)
    
    for item in lst_2:
    
        n_pitch.add(item)
    
    #intialize lists for the two different positions
    pitchers= []
    pos_players = []

    for item in n_hof:
    
        if item in n_pitch:
        
            pitchers.append(item)
        
        else:
        
            pos_players.append(item)
        
    # join the items in the list with a particular separator  
    pattern = '|'.join(pitchers) 

    #value will be the names in the column that are also in the pattern
    new_hof = lst_1.str.contains(pattern) 
    
    return new_hof



def top_list_x(lst,column, name_column):
    
    """Groups list of names from best to lowest in terms of specific column(category)
    Parameters
    ----------
    lst: list of best pitchers you want to sort
    column: the column by which you want to group players by
    name_column: the column that contains the name of players
    
    Returns
    -------
    top_list_x:list
    
    Retrieves the top 30 players of a specific stat category
    
    """
    
    #sorts dataframe of positional players by games played from highest to lowest
    top_list_x = lst.sort_values(by = column, ascending = 0)
    
    #want top 30 from list
    top_list_x = top_list_x[name_column][0:30]
    
    #removes any values besides name, which is what we want 
    top_list_x = [x for x in top_list_x if not isinstance(x, int)]
    
    return top_list_x




def info_ERA(player_name):
    
    """ Retrieve column from dataseries of corresponding player. 
    
    Parameters
    ----------
    player_name: name of player you want stats about-retrieved from excel file
    
    Returns
    -------
    player_stats:list
    
    The result of extracting column series from dataframe.
    
    """
    
    #convert input player_name to string in order to perform read_csv
    xcelfile = player_name
    xcelfile = xcelfile + '.csv'

    player_info = pd.read_csv(xcelfile)
    
    #retrieve careernaverage of ERA by player
    player_stats = player_info['ERA'].mean()
    
    return player_stats

    
def info_BperSO(player_name):
    
    xcelfile = player_name
    xcelfile = xcelfile + '.csv'

    player_info = pd.read_csv(xcelfile)
    
    #retrieve career avg Batters faced per Strikeout by player
    player_stats = (player_info['BF']/player_info['SO']).mean()
    
    return player_stats


def info_IP(player_name):
    
    xcelfile = player_name
    xcelfile = xcelfile + '.csv'

    player_info = pd.read_csv(xcelfile)
    
    #retrieve career max innings pitched by player
    player_stats = (player_info['IP'].max())
    
    return player_stats


def info_WL(player_name):
    
    xcelfile = player_name
    xcelfile = xcelfile + '.csv'

    player_info = pd.read_csv(xcelfile)
    
    #retrieve career average win loss percentage by player
    player_stats = (player_info['W-L%'].mean())
    
    return player_stats



def nxt_hof(era_pl,bperso_pl, wl_pl,era,bperso,wl):
    
    """Compare each category to the average of hof pitchers to count how many times each 2015 pitcher outperfromed a hall of famer.
    
    Parameter
    ---------
    era_pl: dictionary of pitchers and their respective era stats
    bperso_pl: dictionary of pitchers and their respective B per SO stats
    wl_pl: dictionary of pitchers and their respective win loss percentage
    era: starting pitchers and their associated ERA stats
    bperso: starting pitchers and their associated B per SO stats
    wl: starting pitchers and their associated win loss percentage
    
    Returns
    -------
    nxt_hof: dict
    
    Counter: Name and freqyency for each player which indicate the number of times they did better than the avg of a HOF pitcher.
   
    
    """
    
    #initialize new lists
    n_era_players = []
    n_b_perso_players= []
    n_WL_players = []

    #loop through each dictionary value and if it is greater than that of the avg statistical category... 
    #of a hof pitcher, place the dictionary key (name of pitcher) into the list
    
    for item in era_pl:
        
        if era_pl[item] > era.mean():
            
            n_era_players.append(item)
            
    for item in bperso_pl:
        
        if bperso_pl[item] > bperso.mean():
            
            n_b_perso_players.append(item)
            
    for item in wl_pl:
        
        if wl_pl[item] > wl.mean():
            
            n_WL_players.append(item)

#combine all lists
    above_avg = n_era_players + n_b_perso_players + n_WL_players

#count how many times each name appears in list
    nxt_hof = collections.Counter(above_avg)
    
    return print(nxt_hof)