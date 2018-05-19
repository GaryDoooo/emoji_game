import term_io
import os
from account_manage import account, load_account

def send_points(points=100):
    print("""
    You entered the Bank. It's quite empty.
    You see a couple of point sending machines.
    You also see a large cube. On one face of it, it has a screen. 
    It seems like you can check your bank account on it.
    """)
    user_list = os.popen(
        'find vending_accounts/ -name "*.p" |  grep -oP "(?<=vending_accounts/)\w+"').read().split("\n")[:-1]
    while True:
        print("YOU HAVE ### POINTS NOW.")
        try:
            receiver=input("SEND TO WHO:")
            if receiver in user_list:
                print("FOUND USER")
                receiver_user=load_account(receiver)
                amount=int(input("HOW MUCH TO SEND?"))
                if (amount<=points and amount >=0):
                    points=points - amount
                    receiver_user.points +=amount
                    receiver_user.save()
                    print("SENT ### POINTS TO ### SUCCESSFULLY.")
                else:
                    print("Wrong value or not enough points to send.")
            else:
                print("USER NOT FOUND")
            print("KEEP TRYING?")
            if not term_io.y_or_n():
                break
        except ValueError:
            print("Wrong inputs.")
        
    return points

def main():
    send_points(200)

if __name__ == "__main__":
    main()
    
# You see two horizontal lines on the screen on the cube. It tells you to enter your username and password.
# You did it. The screen opens like a giant door.

# You go inside the giant cube, you see a glass ledge. It has nothing on it. 

# You decide to leave the cube. After you came out, the door closed behind you. The original interface with username and password now showes on the screen again.

# You decide to further explore the cube. Inside the cube it's pretty bright; screen on all sides of the walls. One of them showes all of your points. The 2nd one wall is the wall with the empty glass ledge on it, on that screen it says  on it. 












