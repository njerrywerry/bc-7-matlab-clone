import numpy as np
from namespace import name_space

class Matrix(object):
    def __init__(self):
        """Initialize matrix object"""
        pass

    def matrix_creation(self, input_):
        """
        Creates matrix from simple input.
        E.g.
        a = [1, 2, 3, 4] creates a one dimensional matrix.
        b = [1, 2, 3;4, 5, 6] creates a 2-by-3 matrix.
        """
        input_ = str(input_)

        # if input_.find('zeros'):
        #     row, col = int(input_[8]), int(input_[10])
        #     return np.zeros((row, col), dtype=np.int16)
        if input_.find(';'):
            input_.replace('[', ''), input_.replace(']', '')
            return np.matrix(input_)
        else:
            arr = np.array(input_)
            return arr

    def add(self, input2):
        """Addition of a matrix and a number"""
        arr = input2.split('+')
        val = name_space.get(arr[0])
        sum_ = val + int(arr[1])
        return sum_

    def transposer(self, inp):
        matr = inp.replace("\'", '')
        val = name_space.get(matr)
        return np.transpose(val)

    def concat(self, mx):
        val1 = name_space.get(mx[1])
        val2 = name_space.get(mx[3])
        if mx.find(',') != -1:
            return np.concatenate((val1, val2), axis=1)
        elif mx.find(';') != -1:
            return np.concatenate((val1, val2), axis=0)
