from terminaltables import SingleTable
import term_io

def print_inventory(emoji, emoji_you_have, title="Your Inventory"):
    newlist = [emoji[1:], emoji_you_have[1:]]
    table = SingleTable(newlist)
    table.inner_row_border = True
    table.inner_heading_row_border = False
    table.title = title
    print(table.table)

def print_welcome_msg():
    print('''
You have gone out to the Emoji Stand.
You see a lot of emojis in a circle, around an old man.
He smiles at you, he says "Need anything?" 
''')

def selling(points, price, emoji, emoji_you_have):
    while True:
        print_welcome_msg()
        print_inventory(emoji, emoji_you_have)
        message='You have %d points.'
        print(message%points)
        try:
            item_to_sell = int(
                input("Which emoji do you want sell? (please input 1-6): "))
            if (emoji_you_have[item_to_sell]>0):
                # print("ARE YOU SURE TO SELL ### FOR ### POINTS?")
                # print("example %s" % viable )
                print("Are you sure to sell %s" % emoji[item_to_sell],
                       "for %d points?" % price[item_to_sell])
                if term_io.y_or_n():
                    points = points + price[item_to_sell]
                    emoji_you_have[item_to_sell] = emoji_you_have[item_to_sell] - 1
            else:
                print(".....!!!")
            print_inventory(emoji, emoji_you_have)
            print("Keep selling?")
            if not term_io.y_or_n():
                break
        except (ValueError, IndexError):
            print("Please enter 1-6.")

    return points, emoji_you_have

def main():
    selling(200,
    [0,20,30,40,50,12,17],
    ["-", "^_^", "T-T", "@_@", "@.@", "*-*", ":P"],
    [0,3,4,0,5,1,1])

if __name__ == "__main__":
    main()