from random import randint
import string

def sneak_attack(lvl):
    """
    Determines how much damage Shadar's sneak attack does. 
    The amount of times she gets to roll for sneak attack increases by one every two levels, from a base of 1.

    """
    print('Is sneak attack triggered?')
    sneak = input()
    if sneak == 'yes':
        sneak_attack_amt = int(round(((lvl + 0.5)/2), 0))      #rounds to the zeroth place and starts level one at 1 attack
        #generates a random number for however many sneak atatcks Shadar has which is based on her level
        sneak_attack_dmg = [(randint(1, 6)) for x in range(sneak_attack_amt)] 
        print(sneak_attack_dmg)
        sneak_attack_dmg = sum(sneak_attack_dmg)
        print(sneak_attack_dmg)
        return int(sneak_attack_dmg)
    elif sneak == 'no':
        return 0
    
    
def proficiency(lvl):
    """
    Determines how much proficienct Shadar is.
    Proficiecny increases by one every fourth level with a base of 2.

    """
    proficiency = int((lvl-1)/4) + 2     
    return proficiency


def to_hit(dex, proficiency):                     
    """Takes the input dex and proficiency and calculates the to hit. Will show the roll before modifiers are added
    so that players can declare crit (a 1 or 20 before modifiers) since that has special ramifications. The results are told to the 
    game master who determines if the hit landed and tells you to proceed."""
    base_roll = randint(1, 20)
    print('before modifiers your roll is ', base_roll)
    base_roll_w_modifiers = int(base_roll + dex + proficiency)
    print('after modifiers your roll is', base_roll_w_modifiers)

    print ('Do you have advantage? input "yes" for advantage, "no" for disadvantage, "none" for a normal roll')
    adv = input()
    if adv == 'yes': 
        check_for_crit = randint(1,20)
        print('before modifiers your score is ', check_for_crit)
        check_for_crit = max(base_roll, check_for_crit)
        print('before modifiers your max roll was a ', check_for_crit)
        check_for_crit_total = check_for_crit + dex + int(proficiency)
        print('after modifiers your adv roll is ', check_for_crit_total)

    elif adv == 'no':                 
        disadv = randint(1,20)
        print('before modifiers your score is ', disadv)
        disadv = min(base_roll, disadv)
        print('before modifiers your lowest roll was ', disadv)
        disadv_total = disadv + dex + proficiency
        print('after modifiers your disadvantage roll is ', disadv_total)
        
    elif adv == 'none':
        return base_roll

def dual_wielding(dex, proficiency):
    """Determines if the character is able to hit with her off hand (aka dual wielding). The procedure is the same as the to_hit 
    function. If the hit doesn't land then the players turn ends."""
    print('Are you using dual wielding?/ do you need to hit again?')
    dual = input()
    if dual == 'yes':
        off_hand = randint(1, 20)
        print('before modifiers your off hand hits for', off_hand)
        off_hand = int(off_hand + dex + int(proficiency))
        print ('after modifiers your off hand strikes for ', off_hand)
    if dual == 'no':
        return ('Your turn is over')
    
def weapons(dex):
    """Shadar has an arsenal of different weapons with different stats. This allows the player to select the weapon they want."""
    
    print("What weapons are you using? options are: 'rad sword', 'rapier', 'crossbow', 'curved dagger', 'nec dagger' and 'silver dagger")
    pick_weapon = input()
    if pick_weapon == 'rad sword':
        weapon_dmg = (randint(1, 8)) + dex
        return weapon_dmg
    elif pick_weapon == 'rapier':
        weapon_dmg = randint(1, 8) + dex
        return weapon_dmg
    elif pick_weapon =='crossbow':
        weapon_dmg = (randint(1, 6)) + dex
        return weapon_dmg
    elif pick_weapon == 'curved dagger': 
        weapon_dmg = (randint(1, 6)) + dex + 1   #has a special damage increase
        return weapon_dmg
    elif pick_weapon == 'nec dagger':
        weapon_dmg = (randint(1, 6)) + dex
        return weapon_dmg
    elif pick_weapon == 'silver dagger': 
        weapon_dmg = (randint(1, 4)) + dex + 2   #has a special damage increase
        return weapon_dmg
    else:
        raise NameError('Sorry you do not have this weapon in your inventory')
    print('with your dominant hand you deal', weapon_dmg, ' damage')

def main_hand_dmg(weapons, dex):
    print("Did you suceed your to_hit roll?")
    roll_for_dmg = input()
    if roll_for_dmg == 'yes':
        weapon_dmg = weapons(dex)
        return weapon_dmg
    elif roll_for_dmg == 'no':
        weapon_dmg = 0
        return weapon_dmg
    
def dual_dmg(weapons, dex):
    """If the dual wielding attack landed then the player needs to know how much damage they deal, which is based on the weapon they       
    use."""
    print('Did your off hand attack hit?')
    
    second_attack = input()
    if second_attack == 'yes':
        off_hand_attack = weapons(dex)
        return off_hand_attack
    elif second_attack == 'no':
        off_hand_attack = 0
        return off_hand_attack