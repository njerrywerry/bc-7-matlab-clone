'''REPL functionality'''

from __future__ import unicode_literals
from prompt_toolkit import prompt
from prompt_toolkit.history import InMemoryHistory
from pygments.lexers import MatlabLexer

from matrix import Matrix
from namespace import workspace, load_workspace, name_space
from parser import parse

def main():
    history = InMemoryHistory()
    load_workspace()

    while True:
        try:
            input_ = prompt('Mini Matlab >>> ', lexer=MatlabLexer, history=history)
            # import pdb; pdb.set_trace()

            if input_ == 'exit':
                workspace()
                break
            else:
                parse(input_)
        except (EOFError, KeyboardInterrupt, SystemExit):
            workspace()
            break


if __name__ == '__main__':
    main()
