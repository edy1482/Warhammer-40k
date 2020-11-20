class unit_price():

    def __init__(self, name, num=1, price=0):
        self.name = name
        self.num = num
        self.price = price

units = {}

units['gargoyles'] = unit_price('gargoyles', price=17.89)
units['termagant'] = unit_price('termagant', price=15.90)
units['hormogaunt'] = unit_price('hormogaunt', price=17.89)
units['hive guard'] = unit_price('hive guard', num=2, price=42.50)
units['tyrant guard'] = unit_price('tyrant guard', price=42.50)
units['haruspex'] = unit_price('haruspex', price=45)
units['maleceptor'] = unit_price('maleceptor', price=45)
units['warriors'] = unit_price('warriors', num=2, price=25.84)
units['screamer-killer'] = unit_price('screamer-killer', price=55)
units['harpy'] = unit_price('harpy', price=39.76)
units['hive tyrant'] = unit_price('hive tyrant', price=27.83)
units['old one eye'] = unit_price('old one eye', price=55)
units['collecting'] = unit_price('star collecting', price=47.71)
units['enemy below'] = unit_price('enemy below', price=48.50)

def pricing():
    total = 0
    for i in units:
        name = units[i].name
        if units[i].num > 1:
            name = units[i].name + 's'
        price = units[i].price * units[i].num
        total += price
        print(name, '£', price)
    
    print('Total price: £', total)
pricing()