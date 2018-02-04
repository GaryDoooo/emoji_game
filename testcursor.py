import curses
import term_io
import time

stdscr = curses.initscr()
stdscr.addstr(0, 0, "RED ALERT!")
stdscr.refresh()

term_io.press_any_key_to_continue()

begin_x = 20
begin_y = 7
height = 20
width = 40
win = curses.newwin(height, width, begin_y, begin_x)
win.scrollok(True)
win.addstr("test")
win.addstr("2222222222222222222")
win.refresh()
for _ in range(100):
    win.addstr("sdlfkajsda;laskdfj;alskdjfa;sldkjfa;sldkfj" + "\n")
    win.refresh()
    time.sleep(0.3)

term_io.press_any_key_to_continue()

curses.endwin()
