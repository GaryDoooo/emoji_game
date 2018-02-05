import _thread
import time
import curses
#import term_io as ti
import subprocess as sp
import os
# Define a function for the thread
# import re


class chatroom:
    def __init__(self, name="default"):
        self.name = name
        stdscr = curses.initscr()
        curses.cbreak()
        curses.noecho()
        stdscr.keypad(1)

        height, width = stdscr.getmaxyx()
        self.running = True
        self.input_width = width - 10

        self.name_win = curses.newwin(1, 7, 1, 1)
        self.name_win.addstr("INPUT:")
        self.name_win.refresh()
        self.man_win = curses.newwin(2, width, 3, 1)
        self.man_win.addstr(
            "press ENTER to send message. BACKSPACE to modify. type \"exit\" and ENTER to exit...")
        self.man_win.refresh()
        self.input_win = curses.newwin(1, self.input_width, 1, 9)
        self.log_win = curses.newwin(min(40, height - 6), width - 2, 5, 1)
        self.log_win.scrollok(True)

        try:
            _thread.start_new_thread(self.timer1, ("Thread-1", 0.5, ))
        except:
            print("Error: unable to start thread")

    def close(self):
        self.running = False
        time.sleep(1)
        curses.endwin()

    def timer1(self, threadName, delay):
        while self.running:
            time.sleep(delay)
            self.log_win.clear()
            chatlog = sp.check_output(
                ['tail', '-n', '40', 'vending_accounts/chat.log']).decode("utf-8")
            #self.log_win.addstr("%s: %s\n" % ( threadName, time.ctime(time.time()) ))
            self.log_win.addstr(chatlog)
            self.log_win.refresh()

# Create two threads as follows


def run_chatroom(name="default"):
    room = chatroom(name)
    cursor = 0
    square = chr(0x2588)
    inputstr = ""
    while 1:
        room.input_win.clear()
        room.input_win.addstr(inputstr + square)
        room.input_win.refresh()
        char = room.input_win.getch()
        if char in [curses.KEY_ENTER, ord('\n')]:
            # sp.check_output(["echo", "\"" + inputstr + "\"",
            #                 ">>", "vending_accounts/chat.log"])
            #self.log_win.addstr("%s: %s\n" % ( threadName, time.ctime(time.time()) ))
            output = "[" + time.ctime(time.time())[
                4:-8] + "] " + name + ": " + inputstr.replace("\\", "\\\\").replace("\"", "\\\"")
            os.system("echo \"" + output
                      + "\" >> vending_accounts/chat.log")
            cursor = 0
            if inputstr.upper() in ["EXIT", "QUIT"]:
                room.close()
                return
            inputstr = ""
        elif char in [127, ord('\b'), curses.KEY_BACKSPACE, 'KEY_BACKSPACE', '\b', '\x7f']:
            if cursor > 0:
                cursor -= 1
                inputstr = inputstr[:-1]
        else:
            if cursor < room.input_width:
                if char == 27:
                    room.input_win.getch()
                    room.input_win.getch()
                else:
                    inputstr += chr(char)
                    cursor += 1


def main():
    run_chatroom("Test")
    # print(file_num)


if __name__ == "__main__":
    main()
