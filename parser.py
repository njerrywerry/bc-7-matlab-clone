from matrix import Matrix
from namespace import load_workspace, save_workspace, name_space

def parse(string):
    # import pdb; pdb.set_trace()
    if string in name_space:
        value = name_space.get(string)
        print value
    else:
        mat = Matrix()
        l = string.replace(' ', '')
        if l.find('=') != -1:
            matr = mat.matrix_creation(l[2:])
            name_space[str(l[0])] = matr
            return matr

        if l.find('+') != -1:
            add = mat.add(l)
            print add

        if l.find("\'") != -1:
            tr = mat.transposer(l)
            print tr
