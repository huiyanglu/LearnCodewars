"""
Two fighters, one winner.

https://www.codewars.com/kata/577bd8d4ae2807c64b00045b

Create a function that returns the name of the winner in a fight between two fighters.

Each fighter takes turns attacking the other and whoever kills the other first is victorious. Death is defined as having health <= 0.

Each fighter will be a Fighter object/instance. See the Fighter class below in your chosen language.

Both health and damagePerAttack (damage_per_attack for python) will be integers larger than 0. You can mutate the Fighter objects.

Example:
class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack

    def __str__(self): return "Fighter({}, {}, {})".format(self.name, self.health, self.damage_per_attack)
    __repr__=__str__
    
"""

class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack

    def __str__(self): return "Fighter({}, {}, {})".format(self.name, self.health, self.damage_per_attack)
    __repr__=__str__

def declare_winner(fighter1, fighter2, first_attacker):
    h1 = fighter1.health
    h2 = fighter2.health
    d1 = fighter1.damage_per_attack
    d2 = fighter2.damage_per_attack

    for i in range(1,h1//d2++2):
        if first_attacker == fighter1.name:
            h2 =h2-d1
            if h1>0 and h2>0:
                h1 = h1 -d2
                if h1 > 0 and h2 > 0:
                    i+=1
                else:
                    return fighter2.name
            else:
                return fighter1.name
        else:
            h1=h1-d2
            if h1>0 and h2>0:
                h2=h2-d1
                if h1 > 0 and h2 > 0:
                    i+=1
                else:
                    return fighter1.name
            else:
                return fighter2.name

#print(declare_winner(("Aa",10,2),("Bb",5,4),"Bb"))

#print(declare_winner(("Aa",20,5),("Bb",5,4),"Aa"))

print(declare_winner(Fighter("Aa",30,3),Fighter("Bb",20,5),"Bb"))
