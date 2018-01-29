from account_manage import account
from terminaltables import SingleTable


def print_team(team=[1, 2, 3]):
    emoji = ["-", "^_^", "T-T", "@_@", "@.@", "*-*", ":P"]
    newlist = [[emoji[_] for _ in team]]
    print(newlist)
    table = SingleTable(newlist)
    table.inner_row_border = True
    table.inner_heading_row_border = False
    print(table.table)


def main():
    print_team()


if __name__ == "__main__":
    main()
