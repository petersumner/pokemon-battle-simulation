import json
import math
import random

from pokemon import Pokemon

class Battle():
    
    def __init__(self, trainer1, trainer2):

        with open('resources/pokemon.json') as f:
            self.pokemon_info = json.load(f)
        with open('resources/moves.json') as f:
            self.move_info = json.load(f)
        with open('resources/trainers.json') as f:
            self.trainer_info = json.load(f)
            
        self.home = trainer1
        self.visitor = trainer2
        self.home_party = []
        self.visitor_party = []
        self.turns = 1
        self.winner = ''
        self.battle_over = False
        
        self.load_party_info(self.home, self.home_party)
        self.load_party_info(self.visitor, self.visitor_party)
                
       
    def load_party_info(self, trainer, party):
        for poke in self.trainer_info[trainer]['pokemon']:
            party.append(Pokemon(poke['name'], poke['level'], poke['moves']))
            
    def battle(self):
        x, y = 0, 0
        home_pokemon = self.home_party[x]
        visitor_pokemon = self.visitor_party[y]
        while self.battle_over == False:
            print("Turn: " + str(self.turns))
            print(home_pokemon.name+" "+str(home_pokemon.hp)+" vs "+visitor_pokemon.name+" "+str(visitor_pokemon.hp))
            first = home_pokemon if home_pokemon.speed > visitor_pokemon.speed else visitor_pokemon
            second = home_pokemon if first == visitor_pokemon else visitor_pokemon
            self.take_turn(first, second)
            if second.status == 'alive':
                self.take_turn(second, first)
            
            if home_pokemon.status == 'dead':
                x += 1
                if x < len(self.home_party):
                    home_pokemon = self.home_party[x]
                else:
                    self.battle_over = True
                    self.winner = self.visitor
            if visitor_pokemon.status == 'dead':
                y += 1
                if y < len(self.visitor_party):
                    visitor_pokemon = self.visitor_party[y]
                else:
                    self.battle_over = True
                    self.winner = self.home
            self.turns += 1
            
        print("winner: " + str(self.winner))
            
    def take_turn(self, pokemon, opp):
        move, damage = pokemon.select_move(opp)
        print(pokemon.name+" uses "+move+" for "+str(damage)+" damage")

        opp.take_damage(damage)
        
        