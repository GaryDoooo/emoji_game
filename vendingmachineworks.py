from vendingmachineskin import print_vending_machine
from terminaltables import SingleTable

def print_inventory(emoji,emoji_you_have,title="Your Inventory"):
    newlist=[emoji[1:],emoji_you_have[1:]]
    table=SingleTable(newlist)
    table.inner_row_border = True
    table.inner_heading_row_border=False
    table.title=title
    print(table.table)

def yes_or_no():
     while True:
        yesorno=input("Please type Yes or No: ")
        if (yesorno=="yes" or yesorno=="Yes" or yesorno=="YES"):
            return True
        elif (yesorno != "no" and yesorno != "NO" and yesorno !="No"):
            print("Please input required answer.")
        else:
            return False 

def vending(points,price,emoji,emoji_you_have):
    while True:
        print_vending_machine()
        print_inventory(emoji,emoji_you_have)
        print("Now you have %d points." % points)
        try:
            item_to_buy=int(input("Which emoji do you want? (please input 1-6): "))
            if (points>=price[item_to_buy]):
                print("Are you sure to spend %d to buy item %d?"%(price[item_to_buy],item_to_buy))
                if yes_or_no():
                    points = points - price[item_to_buy]
                    emoji_you_have[item_to_buy]=emoji_you_have[item_to_buy]+1
            else:
                print("You do not have enough points.")
            print_inventory(emoji,emoji_you_have)
            print("Continue shopping?")
            if not yes_or_no():
                break
        except (ValueError, IndexError):
            print("Please enter 1-6.")
            
    return points, emoji_you_have

def main():
    points=400
    price=[0,20,60,100,150,200,250]
    emoji=["-","^_^","T-T","@_@","@.@","*-*",":P"]
    emoji_you_have=[0,0,0,0,0,0,0]
    vending(points,price,emoji,emoji_you_have)


if __name__ == "__main__":
    main()    
