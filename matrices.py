from __future__ import unicode_literals
from prompt_toolkit import prompt
from pygments.lexers import MatlabLexer
import numpy as np

namespace = {}

class Matrix(object):
    def __init__(self):
        pass

    def to_matrix(self, input_):
        tokens = str(val)
        if tokens.find(';') < 0:
            return np.array(tokens)
        else:
            tokens.replace('[', '')
            tokens.replace(']', '')
            return np.matrix(tokens)

    def assign_variable(self, var):
        namespace[str(var[0])] = str(var[1])

    def retreive_variable(self, var2):
        value = namespace.get(str(var2), None)
        return value

def main():
    val = prompt('Mini Matlab $ ')

if __name__ == '__main__':
    main()
