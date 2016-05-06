import numpy as np
from namespace import name_space
from numpy.linalg import inv

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

        if input_.find(';'):
            input_.replace('[', ''), input_.replace(']', '')
            return np.matrix(input_)
        else:
            arr = np.array(input_)
            return arr

    def matrix_creation_using_zeros(self, z):
        """Creates a row-by-column zero matrix."""
        z = str(z)
        row, col = int(z[-4]), int(z[-2])
        result = np.zeros((row, col), dtype=np.int16)
        return result

    def add(self, input2):
        """Addition of a matrix and a number"""
        arr = input2.split('+')
        val = name_space.get(arr[0])
        sum_ = val + int(arr[1])
        return sum_

    def transposer(self, inp):
        """Transpose a matrix."""
        matr = inp.replace("\'", '')
        val = name_space.get(matr)
        return np.transpose(val)

    def concat(self, mx):
        """Conatenate two matrices to form a larger one."""
        val1 = name_space.get(mx[1])
        val2 = name_space.get(mx[3])
        if mx.find(',') != -1:
            return np.concatenate((val1, val2), axis=1)
        elif mx.find(';') != -1:
            return np.concatenate((val1, val2), axis=0)

    def inverser(self, y):
        """Inverse of a matrix"""
        value = name_space.get(y)
        if value.shape == (np.transpose(value)).shape:
            counter = 0
            for i in value:
                counter += 1
            val_inv = inv(value)
            if np.allclose(np.dot(value, val_inv), np.eye(counter)) == np.allclose(np.dot(val_inv, value), np.eye(counter)):
                return val_inv
        else:
            return "Error: Matrix {} is not a square matrix".format(y)
