from random import randint
from time import sleep


class color:
    default = "\033[39m"
    black = " \033[30m"
    red = "\033[31m"
    green = "\033[32m"
    Yellow = "\033[33m"
    blue = "\033[34m"
    magenta = "\033[35m"
    cyan = "\033[36m"

# Hello...... kids... I am back.... put down more lines 5 more in print damage. 5 more in print skip and 5 more in print lose..
# You got it? .I am up stairs in my room. I am on the cloud.... |  Where are you?|   In BEDDDDDD????????
# start working on more lines.... quick. |    You = Bossy  | en... so what???? :D
# LOL I am watching you... you need type %s something... something...OK %s, T_T
# you can leave these lines here... fun to look at in the future. when you grow up, you can understand how stupid you were... ^_______^
# no need the space between %s and comma, Need 3 %s... the first one is attacker, second is target, 3rd one is the target. Jennifer is typing
# Use some new words than "DOGED" did you spell dodge right? It's dodge not doge....
# who is the lazy one on line 41? Jennifer is | period. Line 29 and 40 look good.   | Jennifer typed 40   | very smart.
# we need more and more... KIDS are free labor to write codes! esp. stupid kids. | who is the lazy cursor on Line 42 now?Je what happen? I dont know...
# IDK!!!!!! Let me try to bring them back... save... save... save... save... save your work.... 
# libby on the ipad.? ipad is not so compatible to this website. Use the big big HP lappy.    |   ok | 
# write a line like frozen... ice attack... and shock... lightning attack.. and kick butt? 
# libby geting mouse for computer. 
# and maybe throw a cake on someone's face? or poop? find some new words than DODGE.... nice... cake attack.. new chat aera

# Throw a claymore. get a claymore from nowhere and threw it on to someone. 
# quick finish this attack and we can test the new code. %s was libbied by %d HP (%d left)
#I NEED COPY+ PASTE | you need finish that line. put them into one single line. need %s replace "someone...."
# Are you sure "libbied"? you typed it!!!D!D!D!XD  ! Run IT EVERYBODY!
# Finish the line    |   I'm board. ??? go to the bash window on the left.

def print_damage(attacker="attacker_name", target="target_name", damage=0, HP_left=10):
    line = ["%s kicked %s, %s got hurted by %d HP (%d left).",
            "%s sprayed fire on %s, %s was burned by %d HP (%d left).",
            "%s zapped %s, %s took damage by %d HP (%d left).",
            "%s bombed %s and %s took %d HP (%d left).",
            "%s pounced on %s, %s took %d HP (%d left).",
            "%s kicked %s's buttt, %s is hurted by %d (%d left).",
            "%s got a claymore from nowhere and threw it on to %s, %s was libbied by %d HP (%d left)."
            ]
    i = randint(0, len(line) - 1)
    print(line[i] % (attacker, target, target, damage, HP_left))


def print_skip(attacker="attacker_name", target="target_name"):
    line = ["%s tried to kick %s, %s dodged.",
            "%s tried to spray fire on %s, %s dodged.",
            "%s tried to zapp %s, %s dodged it.",
            "%s tried to bomb %s, %s dodged.",
            "%s tried to pounce on %s, %s dodged.",
            "%s tried to kick %s butt, %s avoided the attack."
            ]
    i = randint(0, len(line) - 1)
    print(color.green + line[i] % (attacker, target, target) + color.default)


def print_lose(loser_name="target"):
    line = ["%s was kicked out of the fighting ring.",
            "%s was \"fired\" out of the arena",
            "%s was eletrouted to the ground",
            "%s ran away...",
            "%s took out a piece of white sheet, and waving~~~ waving~~~"
            ]
    i = randint(0, len(line) - 1)
    print("\n" + color.magenta + line[i] % (loser_name) + color.default)


def attack(attacker, target, attacker_att, target_att, target_HP):
    # speed also helps dodge. If player 1 has double speed of player 2, the % of dodge doubles.
    # luck decides dodge and crtical hits. The default dodge and critical hit % is 20.
    # if one player has double luck the both % doubled.
    # damage = attack * min(1,attack/defense), critical double attack, the initial attack tuned by luck .

    dodge_rate = min(
        0.85, 0.2 * target_att[3] / attacker_att[3] * target_att[4] / attacker_att[4])
    critical_rate = min(0.65, 0.2 * attacker_att[4] / target_att[4])
    dodge = (randint(0, 100) < 100 * dodge_rate)
    critical = (randint(0, 100) < 100 * critical_rate)
    if dodge:
        print_skip(attacker, target)
        return target_HP
    else:
        att = attacker_att[1] * (1 + randint(0, round(70 *
                                                      min(1, attacker_att[4] / target_att[4]))) / 100)
        if critical:
            att = att * 2
            print(color.red + "Critical HIT: ", end="")

        damage = att * min(1, attacker_att[1] / target_att[2])
        target_HP = max(0, target_HP - damage)
        print_damage(attacker, target, damage, target_HP)
        print(color.default, end="")
        return target_HP


def fight_start(p1_name="P1", p2_name="P2",
                p1_att=[425, 225, 125, 55, 55],
                p2_att=[150, 25, 55, 460, 160], pause_time=0.5):
    # player attrs: HP 0, attack 1, defense 2, speed 3, luck 4
    # speed decides attack frequency, each player has an accumulator, which reach each 200, the player will attack
    # HP is inputed HP*50

    HP1 = p1_att[0] * 5
    HP2 = p2_att[0] * 5
    accumulator1 = 0
    accumulator2 = 0
    while True:
        sleep(pause_time)
        accumulator1 += p1_att[3]
        accumulator2 += p2_att[3]
        if accumulator1 > accumulator2:
            while accumulator1 >= 200 or accumulator2 >= 200:
                if accumulator1 >= 200:
                    accumulator1 -= 200
                    HP2 = attack(p1_name, p2_name, p1_att, p2_att, HP2)
                    if HP2 <= 0:
                        print_lose(p2_name)
                        return 1  # return winner number.
                if accumulator2 >= 200:
                    accumulator2 -= 200
                    HP1 = attack(p2_name, p1_name, p2_att, p1_att, HP1)
                    if HP1 <= 0:
                        print_lose(p1_name)
                        return 2  # return winner number.
        else:
            while accumulator2 >= 200 or accumulator1 >= 200:
                if accumulator2 >= 200:
                    accumulator2 -= 200
                    HP1 = attack(p2_name, p1_name, p2_att, p1_att, HP1)
                    if HP1 <= 0:
                        print_lose(p1_name)
                        return 2  # return winner number.
                if accumulator1 >= 200:
                    accumulator1 -= 200
                    HP2 = attack(p1_name, p2_name, p1_att, p2_att, HP2)
                    if HP2 <= 0:
                        print_lose(p2_name)
                        return 1  # return winner number.

    # hello i play more minigame bye  |    The fight is a mini game   |   damage= 'damage  |   I go ZZZZZZZZZ   |'
    # I have water in my mouth so cant talk   |     water because my teeth hurt   |     ?????!!!!!!!


def main():
    # print_damage("P1", "P2", 3, 10)
    fight_start(pause_time=1)


if __name__ == "__main__":
    main()
