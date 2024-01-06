import json
import math
import pokemon
import random
import pokebase as pb

from move import Move

class Pokemon():
    
    def __init__(self, name, level, moves):
        with open('resources/type_chart.json') as f:
            self.type_chart = json.load(f)
            
        self.name = name
        self.level = level
        self.moves = []
        self.type = []
        self.stats = {
            'attack': {'base': 0, 'stage': 0},
            'defense': {'base': 0, 'stage': 0},
            'spattack': {'base': 0, 'stage': 0},
            'spdefense': {'base': 0, 'stage': 0},
            'speed': {'base': 0, 'stage': 0}
        }
        self.status = 'alive'
        
        self.get_pokemon_info()
        self.get_move_info(moves)
        
    def get_pokemon_info(self):
        poke = pb.pokemon(self.name)
        for type in poke.types:
            self.type.append(type.type.name)
        
        self.hp = self.get_scaled_stat(poke.stats[0].base_stat)
        self.stats['attack']['base'] = self.get_scaled_stat(poke.stats[1].base_stat)
        self.stats['defense']['base'] = self.get_scaled_stat(poke.stats[2].base_stat)
        self.stats['spattack']['base'] = self.get_scaled_stat(poke.stats[3].base_stat)
        self.stats['spdefense']['base'] = self.get_scaled_stat(poke.stats[4].base_stat)
        self.stats['speed']['base'] = self.get_scaled_stat(poke.stats[5].base_stat)
            
    def get_scaled_stat(self, stat):
        return math.floor(stat * self.level / 50)
            
    def get_move_info(self, moves):
        for move_name in moves:
            self.moves.append(Move(move_name))
            
    def change_stat(self, stat, change):
        if self.stats[stat]['stage'] == 6 and change > 0:
            print(self.name+'\'s '+stat+' won\'t go higher')
        elif self.stats[stat]['stage'] == -6 and change < 0:
            print(self.name+'\'s '+stat+' won\'t go lower')
        else:
            self.stats[stat]['stage'] += change
            if change == 1:
                print(self.name+'\'s '+stat+' rose')
            elif change == 2:
                print(self.name+'\'s '+stat+' sharply rose')
            elif change == -1:
                print(self.name+'\'s '+stat+' fell')
            elif change == -2:
                print(self.name+'\'s '+stat+' harhly fell')
                
    def get_stat(self, stat):
        base_stat = self.stats[stat]['base']
        stage = self.stats[stat]['stage']
        return base_stat * max(2, 2+stage) / max(2, 2-stage)
                
    def select_move(self, opp):
        move_weights = {}
        for move in self.moves:
            move_weights[move] = self.calculate_base_damage(opp, move)
        chosen_move = max(move_weights, key=move_weights.get)
        chosen_move.pp -= 1
        return move
    
    def calculate_base_damage(self, target, move):
        power = int(move.power)
        move_type = str(move.type)
        damage_class = str(move.damage_class)
        if damage_class == 'physical':
            attack = self.get_stat('attack')
            defense = target.get_stat('defense')
        elif damage_class == 'special':
            attack = self.get_stat('spattack')
            defense = target.get_stat('spdefense')
        else:
            return 0
        damage = ((2*self.level/5 + 2)*power*attack/defense/50 + 2)
        
        #type effectiveness
        for type in target.type:
            damage *= self.type_chart[move_type][type]
            
        #stab
        if move.type in self.type:
            damage *= 1.5
        return math.floor(damage)
        
    def calculate_damage(self, target, move):
        move_type = str(move.type)
        crit = False
        effectiveness = 1
        damage = self.calculate_base_damage(target, move)
        
        # type effectiveness
        for type in target.type:
            effectiveness *= self.type_chart[move_type][type]
            
        # crit
        if random.choice(range(0,10000)) < 625:
            crit = True
            damage *= 1.5
            
        #random
        damage *= random.choice(range(85,100)) / 100
        return math.floor(damage), crit, effectiveness
            
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.status = 'dead'
            print(self.name.capitalize()+" fainted")
            