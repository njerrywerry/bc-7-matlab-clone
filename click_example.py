import click
import numpy as np
import cmd2
from pygments import highlight
from pygments.lexers import MatlabLexer
from pygments.formatters import HtmlFormatter

class MiniMatLab(cmd2.Cmd):

    @click.command()
    @click.option('--row', prompt='Number of rows', default=0, help='Number of rows.')
    @click.option('--col', prompt='Number of columns', default=0, help='Number of columns.')
    def do_zeros(row, col):
        '''Creates a ROW by COLUMN matrix'''
        z = np.zeros((row, col))
        # click.echo(np.int8(z))
        print highlight(z, MatlabLexer(), HtmlFormatter())

    @click.command()
    @click.option('--arr', prompt='Enter list', default=[], help='List to transform into array.')
    def do_matrix(arr):
        '''Transform LIST to matrix'''
        a = np.array(arr)
        print a


    # @click.command()
    # def postloop(self):
    #     print


if __name__ == '__main__':
    MiniMatLab().cmdloop()
