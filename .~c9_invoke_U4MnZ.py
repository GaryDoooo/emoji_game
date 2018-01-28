from random import randint

def print_damage(attacker="attacker_name",target="target_name",damage=0,HP_left=10):
    line=["%s kicked %s, %s got hurted by %d HP (%d left).",
          "%s sprayed fire on %s, %s was burned by %d HP (%d left).",
          "%s zapped %s, %s took damage by %d HP (%d left).",
          "%s bombed %s and %s took %d HP (%d left)."
            ]
    i=randint(0,len(line))
    print(line[i]%(attacker,target,target,damage,HP_left))

def print_skip(attacker="attacker_name",target="target_name"):
    line=["%s tried to kick %s, %s dodged.",
          "%s tried to spray fire on %s, %s doged.",
          "%s tried to zapp %s, %s doged it.",
          "%s tried to bomb %s, %s doged."
            ]
    i=randint(0,len(line))
    print(line[i]%(attacker,target,target))

def print_lose(loser_name="target"):
    line=["%s was kicked out of the fighting ring.",
          "%s was \"fired\" out of the arena",
          "%s was eletrouted to the ground",
          "%s ran away...",
          "%s "
            ]
    i=randint(0,len(line))
    print(line[i]%(loser_name))

def fight_start(p1_name="P1",p2_name="P2",
            p1_att=[125,125,125,125,125],
            p2_att=[100,125,75,160,160]):
    # player attrs: HP, attack, defense, speed, luck
    # speed decides attack frequency, each player has an accumulator, which reach each 200, the player will attack
    # speed also helps dodge. If player 1 has double speed of player 2, the % of dodge doubles.
    # luck decides dodge and crtical hits. The default dodge and critical hit % is 20. 
    # if one player has double luck the both % doubled.
    # damage = attack * max(1,attack/defense), critical double attack.
    # HP is inputed HP*5
    HP1=p1_att[0]*5
    HP2=p2_att[0]*5
    accumulator1=0
    accumulator2=0
    while True:
        accumulator1 += p1_att[3]
        accumulator2 += p2_att[3]
        if accumulator1
            if accumulaotr
        
    
    # hello i play more minigame bye  |    The fight is a mini game   |   damage= 'damage  |   I go ZZZZZZZZZ   |'
    # I have water in my mouth so cant talk   |     water because my teeth hurt   |     ?????!!!!!!!
 
def main():
    print_damage("P1","P2",3,10)
 
if __name__ == "__main__":
    main()
