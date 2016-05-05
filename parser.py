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
            if l[3] not in name_space:
                matr = mat.matrix_creation(l[2:])
                name_space[str(l[0])] = matr
            elif l[3] and l[5] in name_space:
                if (l.find(',') != -1) or (l.find(';') != -1):
                    conc = mat.concat(l[2:])
                    name_space[str(l[0])] = conc

        if l.find('+') != -1:
            add = mat.add(l)
            print add

        if l.find("\'") != -1:
            tr = mat.transposer(l)
            print tr
