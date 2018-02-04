import sys
import tty
import termios


class fgcolor:
    default = "\033[39m"
    black = "\033[30m"
    red = "\033[31m"
    green = "\033[32m"
    Yellow = "\033[33m"
    blue = "\033[34m"
    magenta = "\033[35m"
    cyan = "\033[36m"
    reset = "\033[0m"


class bgcolor:
    black = "\033[40m"
    red = "\033[41m"
    green = "\033[42m"
    yellow = "\033[43m"
    blue = "\033[44m"
    magenta = "\033[45m"
    cyan = "\033[46m"
    reset = "\033[0m"
    white = "\033[47m"


class format:
    bold = "\033[1m"
    underline = "\033[4m"
    dim = "\033[2m"
    reverse = "\033[7m"


class cursor:
    upper_left = "\033[H"
    up = "\033[1A"
    down = "\033[1B"
    right = "\033[1C"
    left = "\033[1D"
    very_left = "\033[1000D"
    #  n here is the step numbers
    #  Up: \u001b[{n}A
    #  Down: \u001b[{n}B
    #  Right: \u001b[{n}C
    #  Left: \u001b[{n}D


class delete:
    whole_screen = "\033[2J"
    until_end_of_screen = "\033[0J"
    to_begin_of_screen = "\033[1J"
    whole_line = "\033[2K"
#
    #  Clear Screen: \u001b[{n}J clears the screen
    #  n=0 clears from cursor until end of screen,
    #  n=1 clears from cursor to beginning of screen
    #  n=2 clears entire screen
    #  Clear Line: \u001b[{n}K clears the current line
    #  n=0 clears from cursor to end of line
    #  n=1 clears from cursor to start of line
    #  n=2 clears entire line


def move_cursor(x, y):
    # print("\033[%d;%dH" % (y, x), end="")
    sys.stdout.write(u"\u001b[%d;%dH" % (y, x))
    # Set Column: \u001b[{n}G moves cursor to column n
    # Set Position: \u001b[{n};{m}H moves cursor to row n column m


def getch():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)


def press_any_key_to_continue():
    print("Press Any Key to Continue...")
    getch()


def direction_and_enter():
    while True:
        char = ord(getch())
        if char == 13:
            return "enter"
        if char == 27 and ord(getch()) == 91:
            char = ord(getch())
            if char == 65:
                return "up"
            if char == 66:
                return "down"
            if char == 67:
                return "right"
            if char == 68:
                return "left"


def select_menu(menu_item,  # it's a list of menu item strs
                # a string of \033[xxxm color or format design
                normal_color=fgcolor.default,
                selection_color=format.reverse):
    len_menu = len(menu_item)
    if len_menu == 0:
        return
    selected = 0
    for i in range(len(menu_item)):
        if i == selected:
            print(fgcolor.reset + selection_color + menu_item[i])
        else:
            print(fgcolor.reset + normal_color + menu_item[i])
    print(cursor.up * len_menu)
    while True:
        key = direction_and_enter()
        if key == "enter":
            print(fgcolor.reset + cursor.down * (len_menu - selected))
            return selected
        elif key == "up" and selected > 0:
            selected -= 1
            print(cursor.up * 2 + cursor.very_left +
                  fgcolor.reset + selection_color + menu_item[selected])
            print(fgcolor.reset + normal_color +
                  menu_item[selected + 1] + cursor.up)
        elif key == "down" and selected < (len_menu - 1):
            selected += 1
            print(cursor.up + cursor.very_left +
                  fgcolor.reset + normal_color + menu_item[selected - 1])
            print(fgcolor.reset + selection_color + menu_item[selected])


def y_or_n():
    print("Press Y(es) or N(o).")
    while True:
        char = ord(getch())
        if char == 89 or char == 121:
            return True
        elif char == 110 or char == 78:
            return False


def main():
    print(select_menu(["1. test", "2. test", "3. test", "4.quit"], normal_color=bgcolor.yellow +
                      fgcolor.blue, selection_color=format.bold + bgcolor.red + fgcolor.black))
    # while True:
    for _ in range(10):
        char = getch()
        print(ord(char))
        if y_or_n():
            print("y")
        else:
            print("n")
    # move_cursor(1, 1)
    # sleep(0.1)
    #   print(direction_and_enter())


if __name__ == "__main__":
    main()
