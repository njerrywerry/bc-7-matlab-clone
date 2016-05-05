from matrix import Matrix
from namespace import load_workspace, save_workspace, name_space

def parse(string):
    if string in name_space:
        value = name_space.get(string)
        print value
    elif string.find('='):
        l = string.replace(' ', '')
        mat = Matrix()
        matr = mat.matrix_creation(l[2:])
        name_space[str(l[0])] = matr
        return matr
