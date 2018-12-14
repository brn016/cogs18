from random import randint
import string

        
def test_dex(dex):
    if not isinstance(dex, int):
        raise TypeError('Dex should be a number')
        

def test_proficiency(lvl):
    if not isinstance(proficiency(lvl), int):
        raise TypeError('proficiency should be of type int')
        
    if lvl>= 1 and lvl<= 4:
        assert proficiency == 2
    elif lvl >=5 and lvl<=8:
        assert proficiency == 3
    elif lvl >= 9 and lvl <= 12:
        assert proficiency == 4
    elif lvl >= 13 and lvl<= 16:
        assert proficiency == 5
    elif lvl >= 17 and lvl<= 20:
        assert proficiency == 6
        
def test_sneak_attack(lvl):
    if lvl>= 1 and lvl <= 2:
        assert sneak_attack == 1
    elif lvl >=3 and lvl <=4:
        assert sneak_attack == 2
    elif lvl >= 5 and lvl <= 6:
        assert sneak_attack == 3
    elif lvl >= 7 and lvl <= 8:
        assert sneak_attack == 4
    elif lvl >= 9 and lvl <= 10:
        assert sneak_attack == 5
    elif lvl >= 11 and lvl <= 12:
        assert sneak_attack == 6
    elif lvl >= 13 and lvl <= 14:
        assert sneak_attack == 7
    elif lvl >= 15 and lvl <= 16:
        assert sneak_attack == 8
    elif lvl >= 17 and lvl <= 18:
        assert sneak_attack == 9
    elif lvl >= 19 and lvl <= 20:
        assert sneak_attack == 10