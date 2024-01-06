import json
import string
from pokemon import Pokemon
class Battle():
    
    def __init__(self, trainer1, trainer2):
        self.home = trainer1
        self.visitor = trainer2
        self.turns = 1
        self.battle_over = False
        self.winner = 'none'
        self.weather = 'none'
        
        with open('resources/trainers.json') as f:
            self.trainer_info = json.load(f)
            
    def battle(self):
        home_poke_num, visitor_poke_num = 0, 0
        home_poke = self.home.party[home_poke_num]
        visitor_poke = self.visitor.party[visitor_poke_num]
        print(self.visitor.name+' has challenged '+self.home.name)
        print(self.home.name+' sent out '+home_poke.name.capitalize())
        print(self.visitor.name+' sent out '+visitor_poke.name.capitalize())
        while self.battle_over == False:
            print("Turn: " + str(self.turns))
            first = home_poke if home_poke.get_stat('speed') > visitor_poke.get_stat('speed') else visitor_poke
            second = home_poke if first == visitor_poke else visitor_poke
            self.take_turn(first, second)
            if second.status == 'alive':
                self.take_turn(second, first)
                
            if home_poke.status == 'dead':
                home_poke_num += 1
                if home_poke_num < len(self.home.party):
                    home_poke = self.home.party[home_poke_num]
                    print(self.home.name+' sent out '+home_poke.name.capitalize())
                else:
                    self.battle_over = True
                    self.winner = self.visitor
            if visitor_poke.status == 'dead':
                visitor_poke_num += 1
                if visitor_poke_num < len(self.visitor.party):
                    visitor_poke = self.visitor.party[visitor_poke_num]
                    print(self.visitor.name+' sent out '+visitor_poke.name.capitalize())
                else:
                    self.battle_over = True
                    self.winner = self.home
        
            self.turns += 1
        
        print("Winner: " + str(self.winner.name)+'\n')
        
    def take_turn(self, pokemon, opp):
        move = pokemon.select_move(opp)
        damage, crit, effectiveness = pokemon.calculate_damage(opp, move)
        print(pokemon.name.capitalize()+" used "+string.capwords(move.name.replace('-',' ')))
        if crit:
            print("A critical hit!")
        if effectiveness > 1:
            print("It's super effective!")
        elif effectiveness < 1:
            print("It's not very effective!")

        opp.take_damage(damage)
