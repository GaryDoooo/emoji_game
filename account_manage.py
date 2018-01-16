import pickle
from vendingmachineworks import yes_or_no
# import subprocess as sp
import os
import getpass
# from terminaltables import SingleTable
import re


class account:
    def __init__(self, username, password, points=0, emoji_you_have=[0, 0, 0, 0, 0, 0, 0]):
        self.username = username
        self.password = password
        self.points = points
        self.emoji_you_have = emoji_you_have

    def save(self):
        pickle.dump(self, open("vending_accounts/" +
                               self.username + ".p", "wb"), protocol=0)

    def print_data(self):
        print("username: " + self.username)
        # print("password: ******")
        print("Having points: %d" % self.points)
        print(self.emoji_you_have[1:])

    def del_account(self):
        os.system("rm vending_accounts/" + self.username + ".p")

    def edit_data(self):
        del_account = False
        while True:
            print("1. Change password.")
            print("2. Delete account.")
            print("3. Change points.")
            print("4. Save changes and exit.")
            print("5. Exit withou saving.")
            action = int(input("Choose(1-3): "))
            if action == 1:
                while True:
                    password = getpass.getpass("Password: ")
                    passwd2 = getpass.getpass("Password again:")
                    if passwd2 == password:
                        break
                self.password = password
                print("Got new password.")
            elif action == 2:
                print("Account will be deleted if save changes.")
                del_account == True
            elif action == 3:
                new_points = int(input("New Points: "))
                self.points = new_points
            elif action == 4:
                if del_account:
                    self.del_account()
                else:
                    self.save()
                break
            elif action == 5:
                break


def print_account_list():
    #  find vending_accounts/ -name "*.p" | wc -l
    print("Total account number:")
    # file_num =
    os.system('find vending_accounts/ -name "*.p" | wc -l')
    print("Account List:")
    # file_num=sp.check_output(['find','vending_accounts/','-name','"*.p"','|','wc','-l'])
    os.system(
        'find vending_accounts/ -name "*.p" |  grep -oP "(?<=vending_accounts/)\w+"')
    #file_list=sp.call("ls vending_accounts/*.p")


def load_account(username=None):
    try:
        if username is None:
            filename = "vending_accounts/" + \
                input("Please input the username: ") + ".p"
        else:
            filename = "vending_accounts/" + username + ".p"
        old_account = pickle.load(open(filename, "rb"))
    except OSError:
        print("Username not found, or IO error.")
        old_account = None
    return old_account


def make_new_account(username=None):
    if username is None:
        while True:
            username = input("Username (letters and numbers only): ")
            if re.match("^[A-Za-z0-9]*$", username):
                break
    while True:
        password = getpass.getpass("Password: ")
        passwd2 = getpass.getpass("Password again:")
        if passwd2 == password:
            break
    print("Are you sure to create the new account " + username + "?")
    if yes_or_no():
        new_account = account(username, password)
        new_account.save()


def main():
    while True:

        print_account_list()

        print("Please choose an action:")
        # print("1. List all accounts.")
        print("1. Create a new account.")
        print("2. View one account.")
        print("3. Edit one account.")
        print("4. Exit.")
        action = int(input("Input (1-4): "))

        if action == 1:
            make_new_account()

        if action == 2:
            old_account = load_account()
            if old_account is not None:
                # print(old_account)
                old_account.print_data()

        if action == 3:
            old_account = load_account()
            if old_account is not None:
                old_account.print_data()
                old_account.edit_data()

        if action == 4:
            break


if __name__ == "__main__":
    main()
