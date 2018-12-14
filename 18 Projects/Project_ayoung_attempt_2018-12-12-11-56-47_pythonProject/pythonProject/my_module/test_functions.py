from random import randint
import string
from my_module import my_functions as fn

        
def test_dex(dex):
    if not isinstance(dex, int):
        raise TypeError('Dex should be a number')
        

def test_proficiency(proficiency):
        
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
        
#def test_sneak_attack(sa.sneak_attack_amt, lvl):
 #   if not isinstance(sneak_attack.sneak_attack_amt, int):
  #      raise TypeError('sneak_attack should be of type int')
        
   # if lvl>= 1 and lvl <= 2:
   #     assert sneak_attack_amt == 1
   # elif lvl >=3 and lvl <=4:
   #     assert sneak_attack_amt == 2
   # elif lvl >= 5 and lvl <= 6:
   #     assert sneak_attack_amt == 3
   # elif lvl >= 7 and lvl <= 8:
    #    assert sneak_attack_amt == 4
   # elif lvl >= 9 and lvl <= 10:
   #     assert sneak_attack_amt == 5
    #elif lvl >= 11 and lvl <= 12:
    #    assert sneak_attack_amt == 6
    #elif lvl >= 13 and lvl <= 14:
     #   assert sneak_attack_amt == 7
   # elif lvl >= 15 and lvl <= 16:
   #     assert sneak_attack_amt == 8
   # elif lvl >= 17 and lvl <= 18:
   #     assert sneak_attack_amt == 9
   # elif lvl >= 19 and lvl <= 20:
   #     assert sneak_attack_amt == 10