class unit():

    def __init__(self, name, range_wep = '', side_arm = '', melee_wep = '', gear = '', extra = '', extra_2 = '', extra_3 = '', extra_4 = '', extra_5 = '', num = 1, base_pt = 0, range_wep_pt = 0, side_arm_pt = 0, melee_wep_pt = 0, gear_pt = 0, extra_pt = 0, extra_2_pt = 0, extra_3_pt = 0, extra_4_pt = 0, extra_5_pt = 0, pg_num = 0):
        self.name = name
        self.range_wep = range_wep
        self.side_arm = side_arm
        self.melee_wep = melee_wep
        self.gear = gear
        self.extra = extra
        self.extra_2 = extra_2
        self.extra_3 = extra_3
        self.extra_4 = extra_4
        self.extra_5 = extra_5
        self.num = num
        self.base_pt = base_pt
        self.range_wep_pt = range_wep_pt
        self.side_arm_pt = side_arm_pt
        self.melee_wep_pt = melee_wep_pt
        self.gear_pt = gear_pt
        self.extra_pt = extra_pt
        self.extra_2_pt = extra_2_pt
        self.extra_3_pt = extra_3_pt
        self.extra_4_pt = extra_4_pt
        self.extra_5_pt = extra_5_pt
        self.pg_num = pg_num
#1 gargoyles m
#1 termagant m
#1 hormagaunt m
#2 genestealers, 1 from Collecting, 1 from The Enemy Below m
#2 hive guard m
#1 tyrant guard m
#1 haruspex m
#1 maleceptor m
#2 warriors m
#1 screamer killers m
#trygon prime m, from Collecting
#harpy m
#hive tyrant w/ wings m
#tyranid prime m
#broodlord m, from Collecting
#old one eye m
units = {}
#hq
units['swarmlord'] = unit('swarmlord', melee_wep='bone sabres', side_arm='prehensile pincer tail', base_pt=300, pg_num=86)
units['hive tyrant w/wings'] = unit('hive tyrant w/wings', range_wep='heavy venom cannon', melee_wep='monstrous boneswords', side_arm='prehinsile pincer tail', gear='toxin sacs', base_pt=170, range_wep_pt=25, melee_wep_pt=20, gear_pt=4, pg_num=85)
units['broodlord'] = unit('broodlord', melee_wep='monstrous rending claws', num=2, base_pt=162, pg_num=84)
units['tyranid prime'] = unit('tyranid prime',range_wep='deathspitter', side_arm='flesh hooks', melee_wep='boneswords', gear='toxin sacs', base_pt=100, range_wep_pt=5, side_arm_pt=2, melee_wep_pt=2, gear_pt=4, pg_num=86)
units['old one eye'] = unit('old one eye', melee_wep='monstrous crushing claws', side_arm='monstrous scything talons', gear='thresher scythe', base_pt=200, pg_num=88)

#troops
units['hormagaunt'] = unit('hormagaunt', melee_wep='scything talons', gear='toxin sacs', num=48, base_pt=5, gear_pt=2, pg_num=90)
units['termagant'] = unit('termagant', range_wep='devourer', gear='toxin sacs', num=48, base_pt=4, range_wep_pt=4, gear_pt=1, pg_num=90)
units['genestealer'] = unit('genestealer', melee_wep='rending claws', gear='toxin sacs', extra='extended carapaces', num=24, base_pt=10, melee_wep_pt=2, gear_pt=4, extra_pt=2, pg_num=89)
units['genestealer w/acid maw'] = unit('genestealer', melee_wep='rending claws', side_arm='acid maw', gear='toxin sacs', extra='extended carapaces', num=6, base_pt=10, melee_wep_pt=2, gear_pt=4, extra_pt=2, pg_num=89)
units['genestealer w/flesh hooks'] = unit('genestealer', range_wep='flesh hooks', melee_wep='rending claws', gear='toxin sacs', extra='extended carapaces', num=6, base_pt=10, range_wep_pt=2, melee_wep_pt=2, gear_pt=4, extra_pt=2, pg_num=89)
units['ripper swarm'] = unit('ripper swarm', range_wep='spinemaws', melee_wep='claws and teeth', num=3, base_pt=11, range_wep_pt=2, pg_num=91)
units['tyranid warriors'] = unit('tyranid warriors', range_wep='deathspitter', side_arm='flesh hooks', melee_wep='boneswords', gear='toxin sacs', num=4, base_pt=20, range_wep_pt=5, side_arm_pt=2, melee_wep_pt=2, gear_pt=4, pg_num=89)
units['tyranid warriors'] = unit('tyranid warriors', range_wep='venom cannon', side_arm='flesh hooks', melee_wep='boneswords', gear='toxin sacs', num=1, base_pt=20, range_wep_pt=20, side_arm_pt=2, melee_wep_pt=2, gear_pt=4, pg_num=89)

#elites
units['hive guard'] = unit('hive guard', range_wep='impaler cannon', gear='toxin sacs', num=6, base_pt=18, range_wep_pt=30, gear_pt=1, pg_num=92)
units['tyrant guard'] = unit('tyrant guard', melee_wep='rending claws', side_arm='crushing claws', gear='toxin sacs', num=3, base_pt=35, melee_wep_pt=2, side_arm_pt=12, gear_pt=1, pg_num=92)
units['haruspex'] = unit('haruspex', range_wep='grasping tongue', melee_wep='ravenous maw', side_arm='shovelling claws', base_pt=198, pg_num=96)
units['maleceptor'] = unit('maleceptor', melee_wep='massive scything talons', base_pt=162, melee_wep_pt=10, pg_num=94)

#heavy support
units['trygon prime'] = unit('trygon prime', range_wep='bio-electric pulse with containment spines', melee_wep='massive scything talons', side_arm='toxinspike', gear='toxin sacs', num=2, base_pt=108, melee_wep_pt=60, side_arm_pt=1, gear_pt=8, pg_num=106)
units['carnifex'] = unit('carnifex', range_wep='heavy venom cannon', melee_wep='monstrous scything talons', side_arm='tusks', gear='bone mace', extra='spore cysts', extra_2='chitin thorns', extra_3='toxin sacs', num=2, base_pt=67, range_wep_pt=25, melee_wep_pt=14, side_arm_pt=8, gear_pt=2, extra_pt=10, extra_2_pt=5, extra_3_pt=4, pg_num=102)
units['screamer-killer'] = unit('screamer-killer', range_wep='bio-plasmic scream', melee_wep='monstrous scything talons', gear='toxin sacs', extra='spore cysts', num=2, base_pt=90, melee_wep_pt=15, gear_pt=4, extra_pt=10, pg_num=103)
units['tyrannofex'] = unit('tyrannofex', range_wep='rupture cannon', side_arm='stinger salvoes', melee_wep='powerful limbs', gear='toxin sacs', base_pt=181, range_wep_pt=49, side_arm_pt=8, gear_pt=1, pg_num=100)

#fast attack
units['gargoyle'] = unit('gargoyle', range_wep='flesh borer', melee_wep='blinding venom', num=20, base_pt=6, pg_num=97)
units['ravener'] = unit('ravener', range_wep='deathspitter', melee_wep='rending claws', side_arm='scything talons', num=3, base_pt=23, range_wep_pt=5, melee_wep_pt=2, side_arm_pt=0, pg_num=98)

#flyer
units['harpy'] = unit('harpy', range_wep='2 heavy venom cannons', side_arm='stinger salvo', melee_wep='scything wings', base_pt=121, range_wep_pt=50, side_arm_pt=8, pg_num=109)

def counter():
    pts = 0
    models = 0
    for i in units:
        models += units[i].num
        pts += units[i].num*(units[i].base_pt + units[i].range_wep_pt + units[i].side_arm_pt + units[i].melee_wep_pt + units[i].gear_pt + units[i].extra_pt + units[i].extra_2_pt + units[i].extra_3_pt + units[i].extra_4_pt + units[i].extra_5_pt)
        cost = units[i].num*(units[i].base_pt + units[i].range_wep_pt + units[i].side_arm_pt + units[i].melee_wep_pt + units[i].gear_pt + units[i].extra_pt + units[i].extra_2_pt + units[i].extra_3_pt + units[i].extra_4_pt + units[i].extra_5_pt)
        if units[i].num > 1:
            x = (units[i].name+'s')
        else:
            x = (units[i].name)       
        y = (units[i].range_wep + '.' + units[i].side_arm + '.' + units[i].melee_wep + '.' + units[i].gear + '.' + units[i].extra + '.' + units[i].extra_2 + '.' + units[i].extra_3 + '.' + units[i].extra_4 + '.' + units[i].extra_5)
        print(units[i].num, x, ';', y, ':', cost, 'pts', '\n', '(See pg', units[i].pg_num, 'for more details)')
    print('Total pts:', pts, " ;", models, "models", '\n', '(See pg 126 for pt values and pg 111 for the armoury)')
counter()

class squad():

    def __init__(self, name, power=0, num=1, squad_type=''):
        self.name = name
        self.power = power
        self.num = num
        self.squad_type = squad_type

squads = {}
squads['broodlord'] = squad('broodlord', power=8, squad_type='hq')
squads['swarmlord'] = squad('swarmlord', power=15, squad_type='hq')

squads['termagants'] = squad('termagants', power=9, num=1, squad_type='troops')
squads['ripper swarms'] = squad('ripper swarms', power=2, num=1, squad_type='troops')
squads['hormagaunts'] = squad('hormagaunts', power=9, num=1, squad_type='troops')
squads['genestealers'] = squad('genestealers', power=8, num=2, squad_type='troops')

squads['hive guard'] = squad('hive guard', power=7, squad_type='elites')

squads['gargoyles'] = squad('gargoyles', power=3, squad_type='fast attack')

squads['trygon prime'] = squad('trygon prime', power=10, squad_type='heavy support')
squads['carnifex'] = squad('carnifex', power=12, num=1, squad_type='heavy support')
squads['tyrannofex'] = squad('tyrannofex', power=11, squad_type='heavy support')

def power():
    power = 0
    for i in squads:
        power += (squads[i].power*squads[i].num)
        y = (squads[i].power*squads[i].num)
        if squads[i].num > 1:
            x = (squads[i].name+'s')
        else:
            x = squads[i].name
        print(squads[i].num, x, "\n", "power:", y)
    print("Total Power:", power)
    print("")
#power()

def command():
    #counters
    hq = 0
    troops = 0
    fast_attack = 0
    elites = 0
    heavy_support = 0
    for i in squads:
        #definitions
        squad_type = squads[i].squad_type
        num = squads[i].num
        
        if squad_type == 'hq':
            hq += 1*num
        elif squad_type == 'troops':
            troops += 1*num
        elif squad_type == 'fast attack':
            fast_attack += 1*num
        elif squad_type == 'elites':
            elites += 1*num
        elif squad_type == 'heavy support':
            heavy_support += 1*num
    
    print(hq, "hq")
    print(troops, "troops")
    print(fast_attack, "fast attack")
    print(elites, "elites")
    print(heavy_support, "heavy support")
#command()``