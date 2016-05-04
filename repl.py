'''REPL functionality'''

from __future__ import unicode_literals
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from pygments.lexers import MatlabLexer

import pickle
from matrix import save_workspace, load_workspace
import matrix

def main():
    # history = FileHistory(filename='filename.mat')
    load_workspace()

    while True:
        input_ = prompt('Mini Matlab >>> ', lexer=MatlabLexer)
        if input_ == 'exit':
            workspace()
            break


def workspace():
    """Saves workspace file to load on next session."""
    acknowledge = raw_input('Do you want to save your work? y/n ')
    if acknowledge == 'y':
        save_workspace()
        print 'Workspace saved. Goodbye!'
    elif acknowledge == 'n':
        print 'Goodbye...'

if __name__ == '__main__':
    main()
