from account_manage import account
#from terminaltables import SingleTable
import team
from random import randint
from bs4 import BeautifulSoup
import requests
import re
from vendingmachineworks import yes_or_no
from fight import fight_start


def name_gen():
    url = "https://www.behindthename.com/random/random.php?number=1&gender=both&surname=&all=no&usage_roma=1&usage_fairy=1&usage_trans=1"
    reading = requests.get(url)
    soup = BeautifulSoup(reading.text, "lxml")
#    print(reading.text)
    spans = soup.find_all('span', {'class': 'heavyhuge'})
    return re.sub('[^a-zA-Z]+', '', spans[0].get_text())
    # for s in spans:
    #    print(s.get_text())


def training_room(user):
    level = 1
    while True:
        print("\nYou come to the level %d of the training tower." % level)
        print("The tower was built before the history. It's tall into the the cloud. No one knows where it leads to.")
        trainer_name = name_gen()
        print("The trainer in this level is %s." % trainer_name)
        trainer_team = [randint(1, 6), randint(1, 6), randint(1, 6)]
        team.print_team(trainer_team)
        print("\nNow pick your team to fight with %s." % trainer_name)
        player_team = team.pick_team(user)
        if len(player_team) == 3:
            print("%s's team:" % trainer_name)
            team.print_team(trainer_team)
            print("Your team:")
            team.print_team(player_team)
            print("Start to fight?")
            if yes_or_no():
                winner = fight_start(
                    user.username, trainer_name,
                    team.cal_att(player_team),
                    team.cal_att(trainer_team))
                if winner == 2:
                    print(
                        "You can't move to the next level, and have been sent back the to entance.")
                    return user
                else:
                    level += 1
        else:
            print("Do you want to leave the tower?")
            if yes_or_no():
                return user


def main():
    user = account("test", "test")
    user.emoji_you_have = [3] * 7
    training_room(user)
    # name_gen()
    print("get name")
    print(name_gen())
    print("done")


if __name__ == "__main__":
    main()
