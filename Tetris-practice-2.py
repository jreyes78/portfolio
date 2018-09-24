import curses
import random as ran
import numpy as np


class App():

    def __init__(self):
        curses.initscr()
        curses.noecho()
        self.win = curses.newwin(22, 12)

    def shapes(self, pos, choice):
        if choice == 0:
            stars = [
            self.win.addstr(pos[0], pos[1], '*'),
            self.win.addstr(pos[0], np.subtract(pos[1], 1), '*'),
            self.win.addstr(pos[0], np.add(pos[1], 1), '*'),
            self.win.addstr(pos[0], np.add(pos[1], 2), '*')
            ]
            for x in stars:
                x
            
        elif choice == 1:
            stars = [
            self.win.addstr(pos[0], pos[1], '*'),
            self.win.addstr(pos[0], np.subtract(pos[1], 1), '*'),
            self.win.addstr(np.add(pos[0], 1), pos[1], '*'),
            self.win.addstr(np.add(pos[0], 2), pos[1], '*')
            ]
            for x in stars:
                x
            
        elif choice == 2:
            stars = [
            self.win.addstr(pos[0], pos[1], '*'),
            self.win.addstr(np.add(pos[0], 1), np.subtract(pos[1], 1), '*'),
            self.win.addstr(np.add(pos[0], 1), np.subtract(pos[1], 1), '*'),
            self.win.addstr(np.add(pos[0], 2), np.add(pos[1], 2), '*')
            ]
            for x in stars:
                x
            
        elif choice == 3:
            stars = [
            self.win.addstr(pos[0], pos[1], '*'),
            self.win.addstr(pos[0], np.add(pos[1], 1), '*'),
            self.win.addstr(np.add(pos[0], 1), pos[1], '*'),
            self.win.addstr(np.add(pos[0], 1), np.add(pos[1], 1), '*')
            ]
            for x in stars:
                x
            
        elif choice == 4:
            stars = [
            self.win.addstr(pos[0], pos[1], '*'),
            self.win.addstr(pos[0], np.add(pos[1], 1), '*'),
            self.win.addstr(np.add(pos[0], 1), np.add(pos[1], 1), '*'),
            self.win.addstr(pos[0]+2, np.add(pos[1], 1), '*')
            ]
            for x in stars:
                x
            
        elif choice == 5:
            stars = [
            self.win.addstr(pos[0], pos[1], '*'),
            self.win.addstr(np.add(pos[0], 1), pos[1], '*'),
            self.win.addstr(np.add(pos[0], 1), np.subtract(pos[1], 1), '*'),
            self.win.addstr(np.add(pos[0], 1), np.add(pos[1], 1), '*')
            ]
            for x in stars:
                x
            
        elif choice == 6:
            stars = [
            self.win.addstr(pos[0], pos[1], '*'),
            self.win.addstr(np.add(pos[0], 1), pos[1], '*'),
            self.win.addstr(np.add(pos[0], 1), np.add(pos[1], 1), '*'),
            self.win.addstr(pos[0]+2, np.add(pos[1], 1), '*')
            ]
            for x in stars:
                x

    def choice(self):
        choice = ran.randrange(7)
        return choice
    
    def check_position(self):
        curr_choice = self.choice()
        curses.setsyx(1,5)
        pos = curses.getsyx()
        self.shapes(pos, curr_choice)
        self.win.refresh()
        while True:
            self.win.move(np.add(pos[0], 1), pos[1])
            fall_pos = curses.getsyx()
            self.shapes(fall_pos, curr_choice)
            self.win.refresh()





    def run(self):
        while True:
            self.win.box()
            self.win.keypad(1)
            self.check_position()
            curses.doupdate()
        curses.endwin()

if __name__ == '__main__':
    App().run()