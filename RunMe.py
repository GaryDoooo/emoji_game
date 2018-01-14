from account_login import login_screen
from WelcomeSkin import welcome_print
from vendingmachineskin import print_vending_machine
from vendingmachineworks import print_inventory, vending
from account_manage import account, load_account
from MiniGame_GessingNumbersFull import guess_a_number
import os
from press_any_key import press_any_key_to_continue


def login():
    while True:
        welcome_print()
        user = login_screen()
        if user is not None:
            return user
  # IM DONE!!!!


def print_main_menu():
    # print here. You can use print("v: vending xxxxx")go to figlet|im done
    # Always have the same step here. indent... keep them aligned the start position is minigame 1 word? yes.
    print ('V: Emoji Vending')
    print ('M: Minigames    ')
    # print ('I: Inventory    ')
    print ('S: Show Room    ')
    print ('E: Exit         ')


def show_room():
    emoji = ["-", "^_^", "T-T", "@_@", "@.@", "*-*", ":P"]
    print("You entered the show room. There is a list of users on the wall.")
    a = os.popen(
        'find vending_accounts/ -name "*.p" |  grep -oP "(?<=vending_accounts/)\w+"').read().split("\n")[:-1]
    for user in a:
        user_account = load_account(user)
        print_inventory(emoji, user_account.emoji_you_have,
                        title=user + "'s emoji")
    press_any_key_to_continue()


def main():
    emoji = ["-", "^_^", "T-T", "@_@", "@.@", "*-*", ":P"]
    price = [0, 20, 60, 100, 150, 200, 250]
    user = login()
    while True:
        print_vending_machine()
        print("You have %d points." % user.points)
        print_inventory(emoji, user.emoji_you_have)
        print_main_menu()
        action = input("Please select: ")
        if action == "e" or action == "E":
            user.save()
            return
        if action == "v" or action == "V":
            user.points, user.emoji_you_have = vending(
                user.points, price, emoji, user.emoji_you_have)
            user.save()
        if action == "m" or action == "M":
            print(
                "\n\n\nYou will gain 50 points if winning the game, but lose 5 points if failed.")
            if guess_a_number():
                user.points += 50
            elif user.points >= 5:
                user.points -= 5
            user.save()
            press_any_key_to_continue()
        if action == "s" or action == "S":
            print("\n\n")
            show_room()


if __name__ == "__main__":
    main()
