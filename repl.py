'''REPL functionality'''

from __future__ import unicode_literals
from prompt_toolkit import prompt
from prompt_toolkit.history import InMemoryHistory
from pygments.lexers import MatlabLexer

from matrix import Matrix
from namespace import load_workspace, save_workspace, name_space
from parser import parse

def main():
    history = InMemoryHistory()
    load_workspace()
    while True:
        try:
            input_ = prompt('Mini Matlab >>> ', lexer=MatlabLexer, history=history)
            parse(input_)

            if input_ == 'exit':
                workspace()
                break
        except (EOFError, KeyboardInterrupt, SystemExit):
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
