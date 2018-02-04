from terminaltables import SingleTable
from vendingmachineworks import print_inventory
from term_io import y_or_n as yes_or_no
from account_manage import account
import term_io 
# from press_any_key import press_any_key_to_continue


def cal_att(team):
    if len(team) == 0:
        return [0] * 5
    attribute_table = [[0] * 5] * 6
    # player attrs: HP 0, attack 1, defense 2, speed 3, luck 4
    #^_^ att
    attribute_table[0] = [4, 2, 2, 4, 2]
    # T-T att
    attribute_table[1] = [5, 2, 4, 2, 1]
    #@_@ att
    attribute_table[2] = [3, 5, 3, 1, 2]
    #@.@ att
    attribute_table[3] = [4, 3, 3, 3, 1]
    #*-* att
    attribute_table[4] = [5, 4, 2, 1, 2]
    #:p att
    attribute_table[5] = [1, 2, 1, 5, 5]
    att = [1] * 5
    for i in team:
        i = i - 1
        att = [a * b for a, b in zip(att, attribute_table[i])]
    return att


def print_team(team=[1, 2, 3]):
    if len(team) == 0:
        return
    emoji = ["-", "^_^", "T-T", "@_@", "@.@", "*-*", ":P"]
    newlist = [[emoji[_] for _ in team]]
    # print(newlist)
    table = SingleTable(newlist)
    table.inner_row_border = True
    table.inner_heading_row_border = False
    print(table.table)
    att = cal_att(team)
    att[0] *= 5
    newlist = [["HP", "Attack", "Defense", "Speed", "Luck"]]
    newlist.append(att)
    table = SingleTable(newlist)
    table.inner_row_border = True
    table.inner_heading_row_border = False
    table.title = "Stats"
    print(table.table)


def pick_team(user):
    emoji = ["-", "^_^", "T-T", "@_@", "@.@", "*-*", ":P"]
    team = []
    if sum(user.emoji_you_have[1:]) < 3:
        print("Need at least 3 emojis to form a team.")
        return team
    emoji_list = list(user.emoji_you_have)
    while True:
        print_inventory(emoji, emoji_list)
        #try:
        print("Please choose an emoji to add to your team:")
        choose=term_io.select_menu([
            "    ^_^    ",
            "    T-T    ",
            "    @_@    ",
            "    @.@    ",
            "    *-*    ",
            "     :P    ",
            "  Run Away "])+1
        if 1 <= choose <= 6 and emoji_list[choose] > 0:
            team.append(choose)
            emoji_list[choose] -= 1
        if choose==7:
            team = []
            return team
        #except ValueError:
         #   print("Please key in 1 to 6 to choose an emoji.")
        print("Your current team.")
        print_team(team)
        if len(team) == 3:
            print("You are satisfied with your choices?")
            if yes_or_no():
                return team
            else:
                team = []
                return team


def main():
    print_team()
    user = account("test", "test")
    user.emoji_you_have = [3] * 7
    pick_team(user)


if __name__ == "__main__":
    main()
