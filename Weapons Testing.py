import random
class weapon():
    
    def __init__(self, name='', wep_type='', rolls='', strength='', ap='', damage='', abilities='', pts = 0):
        self.name = name
        self.wep_type = wep_type
        self.rolls = rolls
        self.strength = strength
        self.ap = ap
        self.damage = damage
        self.abilities = abilities
        self.pts = pts
    
weapons = {}
#weapons['macro plasma incinerator'] = weapon(name='macro plasma incinerator', wep_type='heavy', rolls='D6', strength=8, ap=-4, damage='1')
#weapons['heavy onslaught gatling cannon'] = weapon(name='heavy onslaught gatling cannon', wep_type='heavy', rolls=12, strength=5, ap=-1, damage=1)
#weapons['las-talon'] = weapon(name='las-talon', wep_type='heavy', rolls=2, strength=9, ap=-3, damage='D6')
#weapons['heavy Laser destroyer'] = weapon(name='heavy laser destroyer', wep_type='heavy', rolls=2, strength=10, ap=-4, damage='D6', abilities='damage is always 3')
#weapons['storm bolter'] = weapon(name='Storm bolter', wep_type='rapid fire', rolls=4, strength=4, ap=0, damage=1)
#weapons['icarus ironhail heavy stubber'] = weapon(name='icarus ironhail heavy stubber', wep_type='heavy', rolls=3, strength=4, ap=-1, damage=1, abilities='icarus')
weapons['icarus rocket pod'] = weapon(name='icarus rocket pod', wep_type='heavy', rolls='D3', strength=7, ap=-1, damage=2, abilities='icarus')
#weapons['fragstorm grenade launcher'] = weapon(name='fragstorm grenade launcher', wep_type='assault', rolls='D6', strength=4, ap=0, damage=1)
#weapons['heavy flamer'] = weapon(name='heavy flamer', wep_type='heavy', rolls='D6', strength=5, ap=-1, damage=1, abilities='always hit')
#weapons['lightning claws'] = weapon(name='lightning claws', wep_type='melee', rolls=3, strength=4, ap=-2, damage=1, abilities='reroll all wounds')
#weapons['thunder hammer'] = weapon(name='thunder hammer', wep_type='melee', rolls=3, strength=8, ap=-3, damage=3, abilities='-1 from hit roll')
#weapons['bolt rifle'] = weapon(name='bolt rifle', wep_type='rapid fire', rolls=1, strength=4, ap=-1, damage=1)
#weapons['stalker bolt rifle'] = weapon(name='stalker bolt rifle', wep_type='heavy', rolls=1, strength=4, ap=-2, damage=2)
#weapons['plasma incinerator'] = weapon(name='plasma incinerator', wep_type='rapid fire', rolls=1, strength=7, ap=-4, damage=1)
#weapons['heavy plasma incinerator'] = weapon(name='heavy plasma incinerator', wep_type='heavy', rolls=1, strength=8, ap=-4, damage=1)
#weapons['cyclone missile launcher - frag'] = weapon(name='cyclone missile launcher - frag', wep_type='heavy', rolls='2D3', strength=4, ap=0, damage=1)
#weapons['cyclone missile launcher - krak'] = weapon(name='cyclone missile launcher - krak', wep_type='heavy', rolls=2, strength=8, ap=-2, damage='D6')
#weapons['frag grenade'] = weapon(name='frag grenade', wep_type='grenade', rolls='D6', strength=3, ap=0, damage=1)
#weapons['krak grendae'] = weapon(name='krak grenade', wep_type='grenade', rolls=1, strength=6, ap=-1, damage='D3')
#weapons['missile launcher - frag'] = weapon(name='missile launcher - frag', wep_type='heavy', rolls='D6', strength=4, ap=0, damage=1)
#weapons['missile launcher - krak'] = weapon(name='missile launcher - krak', wep_type='heavy', rolls=1, strength=8, ap=-2, damage='D6')
#weapons['assault bolter'] = weapon(name='assault bolter', wep_type='assault', rolls=3, strength=5, ap=-1, damage=1)
#weapons['plasma exterminator'] = weapon(name='plasma exterminator', wep_type='assault', rolls='D3', strength=7, ap=-3, damage=1)
#weapons['flamer'] = weapon(name='flamer', wep_type='assault', rolls='D6', strength=4, ap=0, damage=1, abilities='always hit')
#weapons['meltagun'] = weapon(name='meltagun', rolls=1, strength=8, ap=-4, damage='D6')
#weapons['plasma gun'] = weapon(name='plasma gun', wep_type='rapid fire', rolls=2, strength=7, ap=-3, damage=1)
#weapons['twin lascannon'] = weapon(name='twin lascannon', wep_type='heavy', rolls=2, strength=9, ap=-3, damage='D6')
#weapons['twin heavy bolters'] = weapon(name='twin heavy bolters', wep_type='heavy', rolls=6, strength=5, ap=-1, damage=1)

#Can only do 1 at a time
def output():
    av = []
    for i in range(100000):
        for i in weapons:
            #definitions
            wep_type = weapons[i].wep_type
            rolls = weapons[i].rolls
            strength = weapons[i].strength
            ap = weapons[i].ap
            abilities = weapons[i].abilities
            damage = weapons[i].damage

            no = [] #hits storage
            no_ = [] #wounds storage
            no__ = [] #unsaved wounds storage
            bs = 3 #ballistic skill
            toughness = 4 #enemy toughness
            sv = 3 #enemy save
            assume_move = 0 #assume movement
            fly = 0

            #hit roll
            if abilities == 'icarus':
                if fly == 0:
                    bs += 1
                if fly == 1:
                    bs -= 1
            if abilities == '-1 from hit roll':
                bs += 1
            if wep_type == 'heavy':
                if assume_move == 1:
                    bs += 1
            if rolls == 'D6':
                rolls = random.randint(1,6)
            elif rolls == 'D3':
                die = random.randint(1,6)
                if die == 4 or 5 or 6:
                    rolls = int(round(die/2))
                else:
                    rolls = die
            elif rolls == '2D3':
                die = random.randint(1,6)
                if die == 4 or 5 or 6:
                    die = int(round(die/2))
                die_2 = random.randint(1,6)
                if die_2 == 4 or 5 or 6:
                    die_2 = int(round(die_2/2))
                rolls = die + die_2
            else:
                rolls = int(rolls)
            for i in range(rolls):
                if abilities == 'always hit':
                    no.append('hit')
                    continue
                die = random.randint(1,6)
                if assume_move == 1:
                    if type == 'heavy':
                        bs += 1
                if die >= bs:
                    no.append(die)
                else:
                    continue
            hits = len(no)
            
            #wound roll
            if strength > toughness:
                if strength >= toughness*2:
                    wound = 2
                else:
                    wound = 3
            if strength < toughness:
                if strength <= toughness*0.5:
                    wound = 6
                else:
                    wound = 5
            if strength == toughness:
                wound = 4

            for i in range(hits):
                die = random.randint(1,6)
                if die >= wound:
                    no_.append(die)
                else:
                    if abilities == 'reroll all wounds':
                        die = random.randint(1,6)
                        if die >= wound:
                            no_.append(die)
                        else:
                            continue
                    continue
            wounds = len(no_)

            #save roll
            for i in range(wounds):
                die = random.randint(1,6) + ap
                if die >= sv:
                    continue
                else:
                    no__.append(die)
            total_wounds = len(no__)

            #damage calculation
            total_damage = 0
            for i in range(total_wounds):
                if damage == 'D6':
                    damage = random.randint(1,6)
                    if abilities == 'damage is always 3':
                        if damage == 1 or 2:
                            damage = 3
                elif damage == 'D3':
                    damage = random.randint(1,6)
                    if damage == 4 or 5 or 6:
                        damage = round((damage/2))
                else:
                    damage = int(damage)
                total_damage += damage
            av.append(total_damage)
    for i in weapons:
        print(weapons[i].name)
    #print(av)
    average = sum(av)/len(av)
    print(average)
output()