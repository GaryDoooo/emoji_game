import term_io
import os
from account_manage import account, load_account
import pickle

class bank_acc:
    def __init__(self,name="RECEIVER",amount=0):
        self.name=name
        self.amount=amount
        
    def save(self):
        pickle.dump(self, open("vending_accounts/" +
                               self.name + ".account", "wb"), protocol=0)
                    
    def load(self):
        try:
            filename = "vending_accounts/" + self.name + ".account"
            old_account = pickle.load(open(filename, "rb"))
            self.amount = old_account.amount
            return old_account.amount
        except FileNotFoundError:
            self.amount=0
            return 0


def send_points(user):
    user_list = os.popen(
        'find vending_accounts/ -name "*.p" |  grep -oP "(?<=vending_accounts/)\w+"').read().split("\n")[:-1]
    while True:
        print("YOU HAVE ### POINTS NOW.",user.points)
        try:
            receiver=input("SEND TO WHO:")
            if receiver in user_list:
                print("FOUND USER")
                amount=int(input("HOW MUCH TO SEND?"))
                if (amount<=user.points and amount >=0):
                    user.points -= amount
                    user.save()
                    bank_account=bank_acc(name=receiver)
                    bank_account.load()
                    bank_account.amount += amount
                    bank_account.save()
                    print("SENT ### POINTS TO ### SUCCESSFULLY.",receiver,amount)
                else:
                    print("Wrong value or not enough points to send.")
            else:
                print("USER NOT FOUND")
            print("KEEP TRYING to send more?")
            if not term_io.y_or_n():
                break
        except ValueError:
            print("Wrong inputs.")
        
    return user
    
def cube_explore(user):
    print('''
You decide to further explore the cube. 
        ''')
    while True:
        print('''
Inside the cube it's pretty bright; screen on all sides of the walls. One of them showes all of your points. The 2nd one wall is the wall with the empty glass ledge on it, on that screen it says "NO MAIL"
The third screen says "TAP SCREEN TO BEGIN POINT SHARING". 
        ''')
        action = term_io.select_menu([
        " Sending points ",
        " Leave the cube "])
        if action == 1:
            return user 
        if action ==0:
            user = send_points(user)
            
def collect_point(user):
    amount=0
    bank_account=bank_acc(name=user.username)
    amount=bank_account.load()
    bank_account.amount=0
    bank_account.save()
    user.points+=amount
    user.save()
    return user, amount
    

def operate_screen(user):
    while True:
        print("""
You see two horizontal lines on the screen on the cube. It tells you to enter your username and password.
You did it. The screen opens like a giant door.
        """)
        
        user, points_collected = collect_point(user)
        
        if points_collected ==0:
            print("You go inside the giant cube, you see a glass ledge. It has nothing on it.")
        else:
            print("You go inside the cube there are",points_collected,"points sit on a glass ledge. You take them up and put into your pokect.")
            print("Now you have total", user.points,"points with you.")
        print("\n")
        action = term_io.select_menu([
            " Further explore ",
            "  Leave the cube "])
        if action == 0:
            user = cube_explore(user)
        print("You decide to leave the cube now. After you came out, the door closed behind you. The original interface with username and password now shows on the screen again.")
        return user 

def bank_entry(user):
    while True:
        print("""
You entered the Bank. It's quite empty.
You see a large cube. On one face of it, it has a screen. 
It seems like you can check your bank account on it.
        """)
        action = term_io.select_menu([
            " Operate the screen ",
            "   Exit the bank    "])
        if action == 1:
            return user
        if action == 0:
            user = operate_screen(user)
    

def main():
    # print_team()
    user = account("test", "test")
    user.emoji_you_have = [3] * 7
    user.points=200
    user = bank_entry(user)
    print("you got %d points." % user.points)

if __name__ == "__main__":
    main()
    
# You see two horizontal lines on the screen on the cube. It tells you to enter your username and password.
# You did it. The screen opens like a giant door.

# You go inside the giant cube, you see a glass ledge. It has nothing on it. 

# You decide to leave the cube. After you came out, the door closed behind you. The original interface with username and password now shows on the screen again.

# You decide to further explore the cube. Inside the cube it's pretty bright; screen on all sides of the walls. One of them showes all of your points. The 2nd one wall is the wall with the empty glass ledge on it, on that screen it says "NO MAIL"
# The third screen says "TAP SCREEN TO BEGIN POINT SHARING". 
# You decide to leave the cube now. After you came out, the door closed behind you. The original interface with username and password now shows on the screen again.
