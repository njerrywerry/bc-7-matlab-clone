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

    def math_ops(self, input2):
        """Matrix and array operations"""
        arr = input2.split('+')
        val = name_space.get(arr[0])
        sum_ = val + int(arr[1])
        return sum_
