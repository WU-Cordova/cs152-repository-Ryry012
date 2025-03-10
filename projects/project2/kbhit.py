#!/usr/bin/env python
import sys
import termios
import time
import atexit
from select import select

class KBHit:
    def __init__(self):
        '''Creates a KBHit object that you can call to do various keyboard things.'''
        self.fd = sys.stdin.fileno()
        self.new_term = termios.tcgetattr(self.fd)
        self.old_term = termios.tcgetattr(self.fd)
        # New terminal setting unbuffered
        self.new_term[3] = (self.new_term[3] & ~termios.ICANON & ~termios.ECHO)
        termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.new_term)
        # Support normal-terminal reset at exit
        atexit.register(self.set_normal_term)

    def set_normal_term(self):
        '''Resets to normal terminal.'''
        termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.old_term)

    def getch(self):
        '''Returns a keyboard character after kbhit() has been called.'''
        return sys.stdin.read(1)

    def kbhit(self):
        '''Returns True if keyboard character was hit, False otherwise.'''
        dr, dw, de = select([sys.stdin], [], [], 0)
        return dr != []

# Test
if __name__ == "__main__":
    kb = KBHit()
    print('Hit any key, or ESC to exit')
    iteration = 0
    while True:
        print(f'In loop: {iteration}')
        iteration += 1
        time.sleep(1)
        if kb.kbhit():
            c = kb.getch()
            c_ord = ord(c)
            print(c)
            print(c_ord)
            time.sleep(2)
            if c_ord == 27:  # ESC
                break
