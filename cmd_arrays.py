from cmd2 import Cmd
import numpy as np

class MatLab(Cmd):
    '''Matlab clone'''

    def do_zeros(self, list_):
        a = np.array(list_)
        print a

    def help_zeros(self):
        print '\n'.join(['zeros(row, column)', 'Creates a row-by-column vector of zeros'])

    def do_EOF(self, line):
        return True

    def postloop(self):
        print

if __name__ == '__main__':
    MatLab().cmdloop()
