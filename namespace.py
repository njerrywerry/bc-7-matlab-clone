'''Namespace functionality'''

# import pickle

name_space = {}

def save_workspace(filename='filename.mat'):
    """Save current workspace"""
    file_ = open(filename, 'wb')
    file_.write(str(name_space) + '\n')
    file_.close
    # pickle.dump(name_space, open(filename, 'w'))

def load_workspace(filename='filename.mat'):
    """Loads saved workspace"""
    try:
        file_ = open(filename, 'r')
        v = file_.read()
        file_.close()
        # name_space = pickle.load(open(filename, 'r'))
    except:
        pass