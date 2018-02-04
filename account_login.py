from account_manage import account, load_account, make_new_account
from term_io import y_or_n as yes_or_no
import getpass


def login_screen():
    # username=input("Username: ")
    user = load_account()
    if user is None:
        print("User is not exist. Do you want to make a new one?")
        if yes_or_no():
            make_new_account()
    else:
        password = getpass.getpass("Password ( Your password will not show):")
        if password != user.password:
            print("Username or password is wrong.")
            user = None
    return user


def main():
    while True:
        print("now test the login.")
        user = login_screen()
        if user is not None:
            print("Welcome user %s. " % user.username)
            break


if __name__ == "__main__":
    main()
