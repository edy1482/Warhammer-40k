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

class squad():

    def __init__(self, name, power=0, num=1, squad_type=''):
        self.name = name
        self.power = power
        self.num = num
        self.squad_type = squad_type

squads = {}

squads['captain'] = squad('captain', power=5, num=2, squad_type='hq')
#squads['primaris captain'] = squad('primaris captain', power=5, squad_type='hq')
#squads['primaris chaplain'] = squad('primaris chaplain', power=4, squad_type='hq')
#squads['phobos lieutenant'] = squad('phobos lieutenant', power=4, squad_type='hq')

squads['tactical squad'] = squad('tactical squad', power=7, num=2, squad_type='troops')
#squads['intercessor squad'] = squad('intercessor squad', power=10, num=1, squad_type='troops')
#squads['infiltrator squad'] = squad('infiltrator squad', power=10, num=1, squad_type='troops')
'''
squads['assault squad'] = squad('assault squad', power=5, squad_type='fast attack')
squads['inceptor squad'] = squad('inceptor squad', power=7, squad_type='fast attack')
squads['bike squad'] = squad('bike squad', power=4, num=2, squad_type='fast attack')
squads['suppressor squad'] = squad('suppressor squad', power=4, squad_type='fast attack')

squads['vanguard veteran squad'] = squad('vanguard veteran squad', power=6, squad_type='elites')
squads['sternguard veteran squad'] = squad('sternguard veteran squad', power=6, squad_type='elites')
squads['apothecary'] = squad('apothecary', power=3, squad_type='elites')
squads['company ancient'] = squad('company ancient', power=4, squad_type='elites')
squads['company champion'] = squad('company champion', power=3, squad_type='elites')
squads['company veterans'] = squad('company veterans', power=3, squad_type='elites')
'''
squads['terminator squad'] = squad('terminator squad', power=9, num=3, squad_type='elites')
#squads['terminator assault squad'] = squad('terminator assault squad', power=9, squad_type='elites')

#squads['dreadnought'] = squad('dreadnought', power=5, squad_type='elites')
squads['venerable dreadnought'] = squad('venerable dreadnought', power=6, squad_type='elites')
#squads['ironclad dreadnought'] = squad('ironclad dreadnought', power=7, squad_type='elites')

#squads['aggressor squad'] = squad('aggressor squad', power=5, squad_type='elites')
#squads['redemptor dreadnought'] = squad('redemptor dreadnought', power=10, squad_type='elites')

#squads['devastator squad'] = squad('devastator squad', power=6, squad_type='heavy support')
squads['centurion devastator squad'] = squad('centurion devastator squad', power=12, squad_type='heavy support')
#squads['eliminator squad'] = squad('eliminator squad', power=4, num=2, squad_type='heavy support')
#squads['hellblaster squad'] = squad('hellblaster squad', power=12, num=1, squad_type='heavy support')
squads['predator'] = squad('predator', power=8, squad_type='heavy support')
#squads['repulsor executioner'] = squad('repulsor executioner', power=15, squad_type='heavy support')
#squads['land raider redeemer'] = squad('land raider redeemer', power=14, squad_type='heavy support')

#squads['repulsor'] = squad('repulsor', power=15, squad_type='dedicated transport')

units = {}

units['space marine'] = unit('space marine', range_wep='boltgun', side_arm='bolt pistol', num=14, base_pt=12, pg_num=121)
units['space marine w/flamer'] = unit('space marine', range_wep='flamer', side_arm='bolt pistol', num=2, base_pt=12, range_wep_pt=6, pg_num=121)
units['space marine w/missile launcher'] = unit('space marine', range_wep='missile launcher', side_arm='bolt pistol', num=2, base_pt=12, range_wep_pt=20, pg_num=121)
units['space marine sergeant w/chainsword'] = unit('space marine seargent', side_arm='bolt pistol', melee_wep='chainsword', base_pt=12, pg_num=121)
units['space marine sergeant'] = unit('space marine seargent', range_wep='boltgun', side_arm='bolt pistol', base_pt=12, pg_num=121)
'''
units['devastator sergeant'] = unit('devastator seargent', range_wep='combi-plasma', side_arm='bolt pistol', melee_wep='lightning claw', base_pt=13, range_wep_pt=11, melee_wep_pt=6, pg_num=148)
units['devastator marine w/heavy bolter'] = unit('devastator marine', range_wep='heavy bolter', side_arm='bolt pistol', base_pt=13, range_wep_pt=10, pg_num=148)
units['devastator marine w/lascannon'] = unit('devastator marine', range_wep='lascannon', side_arm='bolt pistol', base_pt=13, range_wep_pt=25, pg_num=148)
units['devastator marine w/plasma cannon'] = unit('devastator marine', range_wep='plasma cannon', side_arm='bolt pistol', base_pt=13, range_wep_pt=16, pg_num=148)
units['devastator marine w/missile launcher'] = unit('devastator marine', range_wep='missile launcher', side_arm='bolt pistol', base_pt=13, range_wep_pt=20, pg_num=148)

units['assault marine sergeant'] = unit('assault seargent', side_arm='plasma pistol', melee_wep='thunder hammer', gear='jump pack', base_pt=15, side_arm_pt=5, melee_wep_pt=16, pg_num=143)
units['assault marine w/plasma pistol'] = unit('assault marine', side_arm='plasma pistol', melee_wep='chainsword', gear='jump pack', base_pt=15, side_arm_pt=5, pg_num=143)
units['assault marine'] = unit('assault marine', side_arm='bolt pistol', melee_wep='chainsword', gear='jump pack', num=3, base_pt=15, pg_num=143)

units['vanguard veteran marine w/hammer'] = unit('vanguard veteran marine', side_arm='storm shield', melee_wep='thunder hammer', gear='jump pack', num=2, base_pt=17, side_arm_pt=2, melee_wep_pt=16, pg_num=133)
units['vanguard veteran marine w/plasma'] = unit('vanguard veteran marine', side_arm='plasma pistol', melee_wep='chainsword', gear='jump pack', base_pt=17, side_arm_pt=5, pg_num=133)
units['vanguard veteran marine w/claws'] = unit('vanguard veteran marine', melee_wep='lightning claws', gear='jump pack', base_pt=17, melee_wep_pt=10, pg_num=133)
units['vanguard veteran sergeant'] = unit('vanguard veteran seargent', side_arm='grav-pistol', melee_wep='relic blade', base_pt=17, side_arm_pt=8, melee_wep_pt=9, pg_num=133)

units['sternguard veteran sergeant'] = unit('sternguard veteran seargent', range_wep='special issue boltgun', side_arm='bolt pistol', melee_wep='power fist', base_pt=14, melee_wep_pt=9, pg_num=134)
units['sterngurad veteran marine w/heavy bolter'] = unit('sternguard veteran marine', range_wep='heavy bolter', side_arm='bolt pistol', base_pt=14, range_wep_pt=10, pg_num=134)
units['sternguard veteran marine w/heavy flamer'] = unit('sternguard veteran marine', range_wep='heavy flamer', side_arm='bolt pistol', base_pt=14, range_wep_pt=14, pg_num=134)
units['sternguard veteran marine w/storm bolter'] = unit('sternguard veteran marine', range_wep='storm bolter', side_arm='bolt pistol', melee_wep='combat knife', base_pt=14, range_wep_pt=2, pg_num=134)
units['sternguard veteran marine w/combi-melta'] = unit('sternguard veteran marine', range_wep='combi-melta', side_arm='bolt pistol', base_pt=14, range_wep_pt=15, pg_num=134)
'''
units['captain w/banner'] = unit('captain', range_wep='master-crafted boltgun', side_arm='bolt pistol', melee_wep='power sword', base_pt=74, range_wep_pt=3, melee_wep_pt=4, pg_num=112)
units['captain'] = unit('captain', range_wep='master-crafted boltgun', side_arm='bolt pistol', melee_wep='lightning claw', base_pt=74, range_wep_pt=3, melee_wep_pt=6, pg_num=112)
'''
units['apothecary'] = unit('apothecary', range_wep='bolt pistol', melee_wep='chainsword', base_pt=50, pg_num=125)
units['company ancient'] = unit('company ancient', range_wep='bolt pistol', base_pt=63, pg_num=126)
units['company champion'] = unit('company champion', range_wep='bolt pistol', melee_wep='master-crafted power sword', gear='combat shield', base_pt=40, melee_wep_pt=6, gear_pt=1, pg_num=127)
units['veteran sergeant'] = unit('veteran sergeant', range_wep='bolt gun', melee_wep='power fist', base_pt=14, melee_wep_pt=9, pg_num=127)
units['space marine veteran'] = unit('space marine veteran', range_wep='meltagun', side_arm='bolt pistol', base_pt=14, range_wep_pt=14, pg_num=127)
'''
units['terminator'] = unit('terminator', range_wep='storm bolter', melee_wep='power fist', num=7, base_pt=23, range_wep_pt=2, melee_wep_pt=9, pg_num=129)
units['terminator w/chainfist'] = unit('terminator', range_wep='storm bolter', melee_wep='chainfist', num=2, base_pt=23, range_wep_pt=2, melee_wep_pt=11, pg_num=129)
units['terminator sergeant'] = unit('terminator seargent', range_wep='storm bolter', melee_wep='power sword', num=3, base_pt=23, range_wep_pt=2, melee_wep_pt=4, pg_num=129)
units['terminator w/heavy flamer'] = unit('terminator', range_wep='heavy flamer', melee_wep='chainfist', base_pt=23, range_wep_pt=14, melee_wep_pt=11, pg_num=129)
units['terminator w/assault cannon'] = unit('terminator', range_wep='assault cannnon', melee_wep='chainfist', base_pt=23, range_wep_pt=22, melee_wep_pt=11, pg_num=129)
units['terminator w/cyclone missile launcher'] = unit('terminator', range_wep='storm bolter', side_arm='cyclone missile launcher', melee_wep='power fist', base_pt=23, range_wep_pt=2, side_arm_pt=32, melee_wep_pt=9, pg_num=129)

#units['assault terminator seargent'] = unit('assault terminator seargent', melee_wep='thunder hammer', gear='storm shield', extra='teleport homer', base_pt=23, melee_wep_pt=16, gear_pt=2, pg_num=130)
#units['assault terminator'] = unit('assault terminator', melee_wep='thunder hammer', gear='storm shield', num=4, base_pt=23, melee_wep_pt=16, gear_pt=2, pg_num=130)

units['devastator centurion seargent'] = unit('devastator centurion seargent', range_wep='heavy bolter', side_arm='heavy bolter', gear='centurion missile launcher', base_pt=40, range_wep_pt=10, side_arm_pt=10, gear_pt=20, pg_num=149)
units['devastator centurion w/grav cannon'] = unit('devastator centurion', range_wep='grav-cannon and grav-amp', side_arm='hurricane bolters', base_pt=40, range_wep_pt=20, side_arm_pt=10, pg_num=149)
units['devastator centurion w/lascannon'] = unit('devastator centurion', range_wep='lascannon', side_arm='lascannon', gear='hurricane bolter', base_pt=40, range_wep_pt=25, side_arm_pt=25, gear_pt=10, pg_num=149)
'''
units['primaris captain'] = unit('primaris captain', range_wep='master-crafted stalker bolt rifle', side_arm='bolt pistol', melee_wep='power sword', base_pt=78, range_wep_pt=5, melee_wep_pt=4, pg_num=110)
#units['primaris chaplain'] = unit('primaris chaplain', side_arm='absolver bolt pistol', melee_wep='crozius arcanum', base_pt=77, pg_num=116)
#units['phobos lieutenant'] = unit('phobos lieutenant', range_wep='master-crafted occulus bolt carbine', side_arm='bolt pistol', melee_wep='paired combat blades', gear='grav-chute', base_pt=90, range_wep_pt=4, gear_pt=2, pg_num=115)
units['intercessor'] = unit('intercessor', range_wep='stalker bolt rifle', side_arm='bolt pistol', num=8, base_pt=17, pg_num=120)
units['intercessor w/auto bolt rifle'] = unit('intercessor', range_wep='auto bolt rifle', side_arm='bolt pistol', gear='auxiliary grenade launcher', base_pt=17, range_wep_pt=1, gear_pt=1, pg_num=120)
units['intercessor sergeant'] = unit('intercessor', range_wep='stalker bolt rifle', side_arm='bolt pistol', base_pt=17, pg_num=120)
#units['eliminator'] = unit('eliminator', range_wep='bolt sniper rifle', side_arm='bolt pistol', gear='camo cloak', num=3, base_pt=18, range_wep_pt=3, gear_pt=3, pg_num=150)
#units['eliminator w/las fusil'] = unit('eliminator', range_wep='las fusil', side_arm='bolt pistol', gear='camo cloak', base_pt=18, range_wep_pt=15, gear_pt=3, pg_num=150)
#units['eliminator sergeant'] = unit('eliminator seargent', range_wep='bolt sniper rifle', side_arm='bolt pistol', gear='camo cloak', num=2, base_pt=18, range_wep_pt=3, gear_pt=3, pg_num=150)
#units['heavy hellblaster'] = unit('hellblaster', range_wep='heavy plasma incinerator', side_arm='bolt pistol', num=4, base_pt=18, range_wep_pt=17, pg_num=151)
#units['hellblaster'] = unit('hellblaster', range_wep='plasma incinerator', side_arm='bolt pistol', num=5, base_pt=18, range_wep_pt=15, pg_num=151)
#units['hellblaster seargent'] = unit('hellblaster sergeant', range_wep='heavy plasma incinerator', side_arm='plasma pistol', base_pt=18, range_wep_pt=17, side_arm_pt=5, pg_num=151)
units['agressor'] = unit('agressor', range_wep='auto bolstorm gauntlets', melee_wep='auto bolstorm gauntlets', side_arm='fragstorm grenade launcher', num=2, base_pt=21, range_wep_pt=12, side_arm_pt=4, pg_num=140)
units['agressor sergeant'] = unit('agressor seargent', range_wep='auto bolstorm gauntlets', melee_wep='auto bolstorm gauntlets', side_arm='fragstorm grenade launcher', base_pt=21, range_wep_pt=12, side_arm_pt=4, pg_num=140)
#units['infiltrator sergeant'] = unit('infiltrator seargent', range_wep='marksman bolt carbine', side_arm='bolt pistol', num=1, base_pt=22, pg_num=122)
#units['infiltrator w/comms'] = unit('infiltrator', range_wep='marksman bolt carbine', side_arm='bolt pistol', gear='infiltrator comms array', base_pt=22, gear_pt=10, pg_num=122)
#units['infiltrator helix adept'] = unit('infiltrator helix adept', range_wep='marksman bolt carbine', side_arm='bolt pistol', base_pt=32, pg_num=122)
#units['infiltrators'] = unit('infiltrator', range_wep='marksman bolt carbine', side_arm='bolt pistol', num=8, base_pt=22, pg_num=122)
units['inceptor sergeant'] = unit('inceptor sergeant', range_wep='plasma exterminator', base_pt=25, range_wep_pt=17, pg_num=144)
units['inceptor'] = unit('inceptor', range_wep='plasma exterminator', num=2, base_pt=25, range_wep_pt=17, pg_num=144)
#units['suppressor sergeant'] = unit('supressor sergeant', range_wep='accelerator autocannon', side_arm='bolt pistol', gear='grav-chute', base_pt=18, range_wep_pt=10, gear_pt=2, pg_num=145)
#units['supressor'] = unit('supressor', range_wep='accelerator autocannon', side_arm='bolt pistol', gear='grav-chute', num=2, base_pt=18, range_wep_pt=10, gear_pt=2, pg_num=145)
'''
#units['dreadnought'] = unit('dreadnought', range_wep='multi-melta', side_arm='storm bolter', melee_wep='dreadnought combat weapon', base_pt=60, range_wep_pt=22, side_arm_pt=2, pg_num=134)
units['venerable dreadnought'] = unit('venerable dreadnought', range_wep='twin lascannon', melee_wep='dreadnought combat weapon', base_pt=80, range_wep_pt=40, pg_num=136)
#units['redemptor dreadnought'] = unit('redemptor dreadnought', range_wep='macro plasma incinerator', side_arm='onslaught gatling gun', melee_wep='redemptor fist', gear='icarus rocket pod', extra='2 storm bolters', base_pt=105, range_wep_pt=31, side_arm_pt=16, gear_pt=6, extra_pt=4, pg_num=137)
#units['ironclad dreadnought'] = unit('ironclad dreadnought', range_wep='hurricane bolter', side_arm='heavy flamer', melee_wep='dreadnought chainfist', gear='2 hunter killer missiles', extra='ironclad assault launchers', base_pt=70, range_wep_pt=10, side_arm_pt=14, melee_wep_pt=28, gear_pt=12, extra_pt=5, pg_num=135)

#units['biker seargent'] = unit('biker seargent', range_wep='twin boltgun', side_arm='bolt pistol', num=2, base_pt=21, range_wep_pt=2, pg_num=142)
#units['space marine biker'] = unit('space marine biker', range_wep='twin boltgun', side_arm='bolt pistol', num=4, base_pt=21, range_wep_pt=2, pg_num=142)
units['predator'] = unit('predator', range_wep='predator autocannon', side_arm='lascannon', melee_wep='lascannon', gear='hunter-killer missile', extra='storm bolter', base_pt=85, range_wep_pt=40, side_arm_pt=25, melee_wep_pt=25, gear_pt=6, extra_pt=2, pg_num=154)
#units['repulsor executioner'] = unit('repulsor executioner', range_wep='heavy laser destroyer', side_arm='heavy onslaught gatling cannon', melee_wep='twin icarus ironhail heavy stubber', gear='auto launchers', extra='twin heavy bolter', extra_2='ironhail heavy stubber', extra_3='icarus rocket pod', extra_4='2 storm bolters', extra_5='2 fragstorm grenade launchers', base_pt=215, range_wep_pt=40, side_arm_pt=30, melee_wep_pt=10, extra_pt=17, extra_2_pt=6, extra_3_pt=6, extra_4_pt=4, extra_5_pt=8, pg_num=158)
#units['repulsor'] = unit('repulsor', range_wep='las-talon', side_arm='twin lascannon', gear='onslaught gatling cannon', extra='ironhail heavy stubber', extra_2='icarus rocket pod', extra_3='6 fragstorm grenade launchers', base_pt=215, range_wep_pt=40, side_arm_pt=40, gear_pt=16, extra_pt=6, extra_2_pt=6, extra_3_pt=24, pg_num=161)
#units['land raider redeemer'] = unit('land raider redeemer', range_wep='twin assault cannon', side_arm='multi-melta', gear='hunter-killer missile', extra='2 flamestorm cannons', base_pt=180, range_wep_pt=44, side_arm_pt=22, gear_pt=6, extra_pt=50, pg_num=157)

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

def command():
    #counters
    hq = 0
    troops = 0
    fast_attack = 0
    elites = 0
    heavy_support = 0
    dedicated_transport = 0
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
        elif squad_type == 'dedicated transport':
            dedicated_transport += 1*num
    
    print(hq, "hq")
    print(troops, "troops")
    print(fast_attack, "fast attack")
    print(elites, "elites")
    print(heavy_support, "heavy support")
    print(dedicated_transport, "dedicated transport")
    print("")

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
    print('Total pts:', pts, " ;", models, "models", '\n', '(See pg 189 for pt values and pg 166 for the armoury)')

power()
command()
counter()