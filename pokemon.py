import json
import math
import pokemon
import random

class Pokemon():
    
    def __init__(self, name, level, moves):
        self.name = name
        self.level = int(level)
        self.status = 'alive'
        self.status = ''

        with open('resources/pokemon.json') as f:
            self.pokemon_info = json.load(f)
        with open('resources/moves.json') as f:
            self.move_info = json.load(f)
        with open('resources/trainers.json') as f:
            self.trainer_info = json.load(f)
        with open('resources/type_chart.json') as f:
            self.type_chart = json.load(f)
                        
        self.type = self.pokemon_info[self.name]['Type']
        
        self.get_stats()
        self.load_moves(moves)
            
    def get_stats(self):
        self.hp = self.get_scaled_stat('HP')
        self.attack = self.get_scaled_stat('Attack')
        self.defense = self.get_scaled_stat('Defense')
        self.spattack = self.get_scaled_stat('Sp. Attack')
        self.spdefense = self.get_scaled_stat('Sp. Defense')
        self.speed = self.get_scaled_stat('Speed')

    def get_scaled_stat(self, stat):
        return math.floor(self.pokemon_info[self.name]['Stats'][stat] * self.level / 50)
    
    def load_moves(self, moves):
        self.moves = {}
        for move in moves:
            self.moves[move] = self.move_info[move]['PP']
    
    def select_move(self, opp):
        move_weights = {}
        valid_moves = [k for k,v in self.moves.items() if v > 0]
        for move in valid_moves:
            weight = self.calculate_damage(opp, move)
            if self.moves[move] <= 0:
                weight = 0
            move_weights[move] = weight
        move = max(move_weights, key=move_weights.get)
        self.moves[move] -= 1
        return move, move_weights[move]
        
    def calculate_damage(self, target, move):
        power = self.move_info[move]['Power']
        move_type = self.move_info[move]['Type']
        if self.move_info[move]['Category'] == 'physical':
            attack = self.attack
            defense = target.defense
        elif self.move_info[move]['Category'] == 'special':
            attack = self.spattack
            defense = target.spdefense
        else:
            return 0
        damage = ((2*self.level/5 + 2)*power*attack/defense/50 + 2)
        #type effectiveness
        for type in target.type:
            damage *= self.type_chart[move_type][type]
        #stab
        if self.move_info[move]['Type'] in self.type:
            damage *= 1.5
        # crit
        if random.choice(range(0,10000)) < 625:
            damage *= 1.5
        #random
        damage *= random.choice(range(85,100)) / 100
        return math.floor(damage)
        
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.status = 'dead'
            print(self.name+" fainted")
        
        