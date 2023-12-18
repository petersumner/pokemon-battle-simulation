import json
from battle import Battle

if __name__ == '__main__':
    
    with open('resources/trainers.json') as f:
        trainers = json.load(f)
        
    
    trainer1 = trainers["Brock"]
    trainer2 = trainers["Misty"]
    
    
    battle = Battle("Brock", "Misty")
    #battle.battle()
    
    battle2 = Battle("Koga", "Sabrina")
    battle2.battle()