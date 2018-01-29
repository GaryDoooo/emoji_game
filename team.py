from terminaltables import SingleTable


def cal_att(team):
    attribute_table = [[0] * 5] * 6
    # player attrs: HP 0, attack 1, defense 2, speed 3, luck 4
    #^_^ att
    attribute_table[0] = [4, 2, 2, 4, 2]
    # T-T att
    attribute_table[1] = [5, 2, 4, 2, 1]
    #@_@ att
    attribute_table[2] = [3, 5, 3, 1, 2]
    #@.@ att
    attribute_table[3] = [4, 3, 3, 3, 1]
    #*-* att
    attribute_table[4] = [5, 4, 2, 1, 2]
    #:p att
    attribute_table[5] = [1, 2, 1, 5, 5]


def print_team(team=[1, 2, 3]):
    emoji = ["-", "^_^", "T-T", "@_@", "@.@", "*-*", ":P"]
    newlist = [[emoji[_] for _ in team]]
    print(newlist)
    table = SingleTable(newlist)
    table.inner_row_border = True
    table.inner_heading_row_border = False
    print(table.table)


if __name__ == "__main__":
    main()
