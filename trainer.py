import json
from pokemon import Pokemon

class Trainer():
    
    def __init__(self, name):
        with open('resources/trainers.json') as f:
            self.trainer_info = json.load(f)
            
        self.name = name
        self.party = []
        
        for poke in self.trainer_info[self.name]['pokemon']:
            self.party.append(Pokemon(poke['name'], poke['level'], poke['moves']))
        
        print("Loaded "+self.name)