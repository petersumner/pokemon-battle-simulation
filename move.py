import pokebase as pb

class Move():
    
    def __init__(self, name):        
        move = pb.move(name)
        
        self.name = move.name
        self.accuracy = move.accuracy
        self.effect_chance = move.effect_chance
        self.pp = move.pp
        self.priority = move.priority
        self.power = move.power
        self.damage_class = move.damage_class
        self.stat_changes = move.stat_changes
        self.target = move.target
        self.type = move.type
        