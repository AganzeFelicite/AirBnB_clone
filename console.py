#!/usr/bin/env python3
"""this is the console module of the hbnb project"""
import cmd
import sys

class HBNBCommand(cmd.Cmd):
    """this is a console"""
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = '(hbnb)'

    def do_quit(self, arg):
        """this is a command to quit the console"""
        sys.exit(1)

    def emptyline(self):
        self.cmdloop()

    #shortcut
    do_EOF = do_quit
if __name__ == '__main__':
    HBNBCommand().cmdloop()
