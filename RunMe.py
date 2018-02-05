from account_login import login_screen
from WelcomeSkin import welcome_print
from vendingmachineskin import print_vending_machine
from vendingmachineworks import print_inventory, vending
from account_manage import account, load_account
import os
import term_io  # press_any_key_to_continue
from training_room import training_room
from minigame_entry import minigame
from chatroom import run_chatroom


def login():
    while True:
        welcome_print()
        user = login_screen()
        if user is not None:
            return user
  # IM DONE!!!!


#  def print_main_menu():
    #  # print here. You can use print("v: vending xxxxx")go to figlet|im done
    #  # Always have the same step here. indent... keep them aligned the start position is minigame 1 word? yes.
    #  print ('V: Emoji Vending')
    #  print ('M: Minigames    ')
    #  print ('T: Training Tower    ')
    #  print ('S: Show Room    ')
    #  print ('E: Exit         ')


def show_room():
    user_account = account("init", "get rid of error msg.")
    emoji = ["-", "^_^", "T-T", "@_@", "@.@", "*-*", ":P"]
    print("You entered the show room. There is a list of users on the wall.")
    a = os.popen(
        'find vending_accounts/ -name "*.p" |  grep -oP "(?<=vending_accounts/)\w+"').read().split("\n")[:-1]
    for user in a:
        user_account = load_account(user)
        print_inventory(emoji, user_account.emoji_you_have,
                        title=user + "'s emoji")
    term_io.press_any_key_to_continue()


def main():
    emoji = ["-", "^_^", "T-T", "@_@", "@.@", "*-*", ":P"]
    price = [0, 20, 60, 100, 150, 200, 250]
    user = login()
    while True:
        print_vending_machine()
        print("You have %d points." % user.points)
        print_inventory(emoji, user.emoji_you_have)
        print("\n--== Main Menu ==--")
        action = term_io.select_menu([
            " Emoji Vending ",
            "   Minigames   ",
            " Ancient Tower ",
            "   Show Room   ",
            "   Chat Room   ",
            "   Exit Game   "])
        if action == 5:
            user.save()
            return
        if action == 4:
            run_chatroom(user.username)
        if action == 0:
            user.points, user.emoji_you_have = vending(
                user.points, price, emoji, user.emoji_you_have)
            user.save()
        if action == 1:
            user = minigame(user)
        if action == 3:
            print("\n\n")
            show_room()
        if action == 2:
            user = training_room(user)


if __name__ == "__main__":
    main()
