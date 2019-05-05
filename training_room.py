from account_manage import account
# from terminaltables import SingleTable
import team
from random import randint
from bs4 import BeautifulSoup
import requests
import re
from fight import fight_start
import term_io


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
    print(term_io.delete.whole_screen + term_io.bgcolor.yellow +
          term_io.fgcolor.black +
          "               The Ancient Tower               " +
          term_io.fgcolor.reset)
    print(
        "You entered an ancient tower. You will meet spirit fighters with their emojis in the tower. You need beat them to move the every next level. You will receive a blessing at each five levels you clear. But be careful that if you lose a battle, you will lose your emojis in the team. So choose the team wisely."
    )
    level = 1
    while True:
        if level != 1:
            if (level - 1) % 5 == 0:
                print(
                    term_io.fgcolor.green +
                    "You come to a blessing spring. After you drink some water in the spring, you feel refreshed."
                )
                print("(Technically, you received %d points.)" %
                      (300 * int(level / 5)) + term_io.fgcolor.reset)
                user.points += 300 * int(level / 5)
            else:
                print(term_io.fgcolor.green + "You gained 10 points." +
                      term_io.fgcolor.reset)
                user.points += 10
            user.save()
        trainer_name = name_gen()
        trainer_team = [randint(1, 6), randint(1, 6), randint(1, 6)]
        while True:
            print(term_io.bgcolor.blue +
                  "\nYou come to the level %d of the tower." % level +
                  term_io.bgcolor.reset)
            print(
                "The tower was built before history. It grows tall into the clouds. No one knows where it leads to."
            )
            print("The trainer in this level is %s." % trainer_name)
            team.print_team(trainer_team)
            print("\nNow pick your team to fight against %s." % trainer_name)
            player_team = team.pick_team(user)
            if len(player_team) == 3:
                print("%s's team:" % trainer_name)
                team.print_team(trainer_team)
                print("Your team:")
                team.print_team(player_team)
                print(
                    "Start to fight? (Remember, if you press F key during the battle, it's some chance to run away from it."
                )
                if term_io.y_or_n():
                    winner = fight_start(user.username, trainer_name,
                                         team.cal_att(player_team),
                                         team.cal_att(trainer_team))
                    if winner == 2:
                        print(
                            "You can't move to the next level, and have been sent back the to entance."
                        )
                        for team_member in player_team:
                            user.emoji_you_have[team_member] -= 1
                            user.save()
                        term_io.press_any_key_to_continue()
                        return user
                    elif winner == 0:
                        print(
                            "You got out of the tower and looked back. There is no one running after you."
                        )
                        term_io.press_any_key_to_continue()
                        return user
                    else:
                        level += 1
                        break
            else:
                print("Do you want to leave the tower?")
                if term_io.y_or_n():
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
