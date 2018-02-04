import _thread
import time
import curses
import term_io as ti
import subprocess as sp

# Define a function for the thread

class chatroom:
   def __init__(self,name="default"):
      self.name=name
      stdscr = curses.initscr()
      curses.noecho()
      height, width = stdscr.getmaxyx()
      self.running=True
      self.input_width=width-10
      
      self.name_win=curses.newwin(1,7,1,1)
      self.name_win.addstr("INPUT:")
      self.name_win.refresh()
      self.input_win=curses.newwin(1,self.input_width,1,9)
      self.log_win=curses.newwin(min(40,height-5),width-2,3,1)
      self.log_win.scrollok(True)
      
      try:
         _thread.start_new_thread( self.timer1, ("Thread-1", 0.5, ) )
      except:
         print("Error: unable to start thread")
   
   def close(self):
      self.running=False
      curses.endwin()
      
   def timer1(self,threadName, delay):
      while self.running:
         time.sleep(delay)
         self.log_win.clear()
         chatlog=sp.check_output(['tail','-n','40','vending_accounts/chat.log']).decode("utf-8") 
         #self.log_win.addstr("%s: %s\n" % ( threadName, time.ctime(time.time()) ))
         self.log_win.addstr(chatlog)
         self.log_win.refresh()

# Create two threads as follows

def run_chatroom(name="default"):
   room=chatroom(name)
   cursor=0
   square=chr(0x2588) 
   inputstr=""
   while 1:
      room.input_win.clear()
      room.input_win.addstr(inputstr+square)
      room.input_win.refresh()
      char=room.input_win.getkey(0,cursor)
      inputstr+=char
      cursor+=len(char)
      

def main():
   run_chatroom("Test")
   #print(file_num)
   
   

if __name__ == "__main__":
    main()