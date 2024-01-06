import json
from battle import Battle
from trainer import Trainer

if __name__ == '__main__':
    '''
    num_matches = 1
        
    brock = Trainer('Brock')
    misty = Trainer('Misty')
    ltsurge = Trainer('Lt. Surge')
    erika = Trainer('Erika')
    koga = Trainer('Koga')
    sabrina = Trainer('Sabrina')
    blaine = Trainer('Blaine')
    giovanni = Trainer('Giovanni')
    
    trainer_pool = [brock, misty, ltsurge, erika, koga, sabrina, blaine, giovanni]
    
    battle_stats = {
        'Brock': {'wins': 0},
        'Misty': {'wins': 0},
        'Lt. Surge': {'wins': 0},
        'Erika': {'wins': 0},
        'Koga': {'wins': 0},
        'Sabrina': {'wins': 0},
        'Blaine': {'wins': 0},
        'Giovanni': {'wins': 0},
    }
    
    #battle = Battle(brock, misty)
    
    for i in range(len(trainer_pool)-1):
        for j in range(i+1, len(trainer_pool)):
            battle = Battle(trainer_pool[i],trainer_pool[j])
            for match in range(num_matches):
                battle.battle()
                battle_stats[battle.winner.name]['wins'] += 1
    '''
    brock = Trainer('Brock')
    ltsurge = Trainer('Lt. Surge')
    battle = Battle(brock, ltsurge)
    battle.battle()
