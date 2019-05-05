# import curses
import term_io
from dungeon_walk import dungeon
from account_manage import account
import dungeon_narrative
from random import randint
import os


class dungeon_screen:

    def __init__(
            self,
            dungeon_name="==== Dungeon ====",
            subtitle="Use Arrow keys to move your butt. ENTER to interact."):
        # stdscr = curses.initscr()
        # curses.cbreak()
        # curses.noecho()
        # stdscr.keypad(1)
        # curses.start_color()
        # stdscr.erase()

        # height, width = stdscr.getmaxyx()
        # self.running = True
        self.map_width = 48
        self.map_height = 15
        self.dungeon_name = dungeon_name
        self.subtitle = subtitle

        self.titles()
        # self.map_win = curses.newwin(self.map_height, self.map_width, 6, 6)

        # self.log_win = curses.newwin(min(10, height - 8+self.map_height), width - 20, 8+self.map_height, 5)
        # self.log_win.scrollok(True)
        # self.log_win.box()
        self.log = [" " for _ in range(4)]
        os.system('setterm -cursor off')

    def titles(self):
        # self.title_win = curses.newwin(1, width, 1, 1)
        # self.title_win.addstr(dungeon_name, curses.A_STANDOUT)
        # self.title_win.refresh()
        print(term_io.delete.whole_screen + term_io.cursor.upper_left +
              term_io.bgcolor.reset + term_io.fgcolor.Yellow +
              self.dungeon_name)

        # self.man_win = curses.newwin(2, width, 3, 1)
        # self.man_win.addstr(
        #     subtitle, curses.A_DIM)
        # self.man_win.refresh()
        print(term_io.format.dim + "\n" + self.subtitle)

    def refresh_map(self, map_string):
        # self.map_win.clear()
        # self.map_win.addstr("map_string",curses.A_STANDOUT)
        # self.map_win.refresh()
        term_io.move_cursor(1, 6)
        print(map_string)
        print(term_io.bgcolor.reset + term_io.fgcolor.default)

    def close(self):
        # self.running = False
        # time.sleep(1)
        # curses.endwin()
        print(term_io.bgcolor.reset + term_io.fgcolor.default +
              term_io.delete.whole_screen)

    def add_log(self, new_info="adding a new line"):
        # self.log_win.addstr(new_info,curses.A_STANDOUT)
        # self.log_win.refresh()
        # max 10 lines
        term_io.move_cursor(1, 6 + self.map_height)
        print(term_io.delete.until_end_of_screen)
        term_io.move_cursor(1, 6 + self.map_height)
        for i in [3, 2, 1]:
            self.log[i] = self.log[i - 1]
        self.log[0] = new_info
        for i in range(4):
            print(self.log[i])

    def menu(self, menu_items):
        return term_io.xy_menu(menu_items, x0=self.map_width + 5, y0=6)


def rand_pick(narratives):
    i = randint(0, len(narratives) - 1)
    return narratives[i]


def menu_action(screen, item):
    action = screen.menu(item.actions)
    screen.add_log(rand_pick(item.narratives[item.actions[action]]))
    return item.actions[action]


def take_action(dun, screen, user, next_block):
    if next_block == 1100:
        menu_action(screen, dungeon_narrative.floor)
    elif next_block == 1000:
        menu_action(screen, dungeon_narrative.wall)
    elif int(next_block / 100) == 13:
        action = menu_action(screen, dungeon_narrative.joke)
        if action == "   Look   ":
            joke = dun.jokes[next_block % 100]
            screen.add_log(term_io.fgcolor.red + joke + term_io.fgcolor.default)
    elif next_block == 1400:
        action = menu_action(screen, dungeon_narrative.stele)
        if action == "   Kick   ":
            user = kick_stele(screen, user)
    return user


def rand_mine(screen, user, rate=40):
    if randint(1, rate) == 1:
        points = randint(2, 5)
        user.points += points
        screen.add_log(term_io.fgcolor.green +
                       "You found %d points on the floor and picked them up." %
                       points + term_io.fgcolor.default)
    return user


def kick_stele(screen, user, rate=10):
    if randint(1, rate) == 1:
        points = randint(2, 50)
        user.points += points
        screen.add_log(
            term_io.fgcolor.green +
            "!!! Something falling off from the top of the stele!!!\n" +
            "They are %d points. You picked them up." % points +
            term_io.fgcolor.default)
    return user


def portal_entry(user):
    dun = dungeon()
    screen = dungeon_screen()
    screen.refresh_map(dun.display_string())
    screen.add_log(rand_pick(dungeon_narrative.enter.portal))
    next_block = 1100
    while True:
        key = term_io.direction_and_enter()
        if key == 'enter':
            user = take_action(dun, screen, user, next_block)
        else:
            events, next_block = dun.move_player(key)
            screen.refresh_map(dun.display_string())
            # print(events)
            for event in events:
                if event == 'moved':
                    user = rand_mine(screen, user, rate=100)
                    # screen.add_log("moved")
                elif event == 'blocked':
                    do_nothing = None
                    # screen.add_log("You can not move there.")
                elif event == 'exit':
                    screen.close()
                    return user


def main():
    user = account("test", "test")
    user.emoji_you_have = [3] * 7
    portal_entry(user)
    # name_gen()


if __name__ == "__main__":
    main()
