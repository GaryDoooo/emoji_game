import pickle
from vendingmachineworks import yes_or_no 
import subprocess as sp
import os

class account:
    def __init__(self,username,password,points=0,emoji_you_have=[0,0,0,0,0,0,0]):
        self.username=username
        self.password=password
        self.points=points
        self.emoji_you_have=emoji_you_have
    
    def save(self):
        pickle.dump(self,open("vending_accounts/"+self.username+".p","wb"),protocol=0)

def print_account_list():
    #  find vending_accounts/ -name "*.p" | wc -l
    print("Total account number:")
    file_num=os.system('find vending_accounts/ -name "*.p" | wc -l')
    print("Account List:")
    #file_num=sp.check_output(['find','vending_accounts/','-name','"*.p"','|','wc','-l'])
    os.system('find vending_accounts/ -name "*.p" |  grep -oP "(?<=vending_accounts/)\w+"')
    #file_list=sp.call("ls vending_accounts/*.p")

def main():
    while True:
        
        print_account_list()
        
        print("Please choose an action:")
        # print("1. List all accounts.")
        print("1. Create a new account.")
        print("2. View one account.")
        print("3. Edit one account.")
        print("4. Exit.")
        action=int(input("Input (1-4): "))
        
        if action==1:
            username=input("Username: ")
            while True:
                password=input("Password: ")
                passwd2=input("Password again:")
                if passwd2==password:
                    break
            print("Are you sure to create the new account "+username+"?")
            if yes_or_no():
                new_account=account(username,password)
                new_account.save()


if __name__ == "__main__":
    main()
