from numpy.random import randint

def print_damage(attacker="attacker_name",target="target_name",damage=0,HP_left=10):
    line=["%s kicked %s, %s got hurted by %d HP (%d left).",
          "%s sprayed fire on %s, %s was burned by %d HP (%d left).",
          "%s zapped %s, %s took damage by %d HP (%d left).",
          "%s "
            ]
    i=randint(0,len(line))
    print(line[i]%(attacker,target,target,damage,HP_left))

def print_skip(attacker="attacker_name",target="target_name"):
    line=["%s tried to kick %s, %s dodged."
            ]
    i=randint(0,len(line))
    print(line[i]%(attacker,target,target))


def fight_start(p1_name="P1",p2_name="P2",
            p1_att=[125,125,125,125,125],
            p2_att=[100,125,75,160,160]):
    return
 # hello i play more minigame bye  |    The fight is a mini game   |   damage= 'damage  |   I go ZZZZZZZZZ   |'
 
def main():
    print_damage("P1","P2",3,10)
 
if __name__ == "__main__":
    main()