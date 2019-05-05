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
from library import library
from sell_emoji import selling
from bank import bank_entry, bank_acc
from dungeon_ctrl import portal_entry


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
        'find vending_accounts/ -name "*.p" |  grep -oP "(?<=vending_accounts/)\w+"'
    ).read().split("\n")[:-1]
    for user in a:
        user_account = load_account(user)
        print_inventory(
            emoji, user_account.emoji_you_have, title=user + "'s emoji")
    term_io.press_any_key_to_continue()


def my_inventory(user, emoji):
    print("\nYou have %d points." % user.points)
    print_inventory(emoji, user.emoji_you_have)
    term_io.press_any_key_to_continue()


def main():
    emoji = ["-", "^_^", "T-T", "@_@", "@.@", "*-*", ":P"]
    price = [0, 20, 60, 100, 150, 200, 250]
    user = login()
    while True:
        # print_vending_machine()
        # print("\n--== Main Menu ==--")
        print(term_io.bgcolor.black + term_io.fgcolor.Yellow)
        os.system("figlet Main Menu")
        print(term_io.bgcolor.black + term_io.fgcolor.default)
        action = term_io.select_menu(
            [
                " Emoji Vending ", "  Emoji Stand  ", "   Minigames   ",
                " Ancient Tower ", "   Show Room   ", " Message Board ",
                "    Library    ", "     Bank      ", "  My Inventory ",
                "  Magic Portal ", "   Exit Game   "
            ],
            front_space=15)
        if action == 10:
            user.save()
            return
        if action == 9:
            print(
                term_io.delete.whole_screen +
                "It is a portal standing on the ground formed with blue light. You can only see light inside it."
            )
            print("You are not sure if stepping into it.")
            if term_io.y_or_n():
                user = portal_entry(user)
        if action == 8:
            my_inventory(user, emoji)
        if action == 6:
            library()
        if action == 5:
            run_chatroom(user.username)
        if action == 0:
            user.points, user.emoji_you_have = vending(
                user.points, price, emoji, user.emoji_you_have)
            user.save()
        if action == 2:
            user = minigame(user)
        if action == 4:
            print("\n\n")
            show_room()
        if action == 3:
            user = training_room(user)
        if action == 1:
            selling_price = [_ / 2 for _ in price]
            user.points, user.emoji_you_have = selling(
                user.points, selling_price, emoji, user.emoji_you_have
            )  #selling price is some rate of buying price
            user.save()
        if action == 7:
            user = bank_entry(user)
            user.save()


if __name__ == "__main__":
    main()
