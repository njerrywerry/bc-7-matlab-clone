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

def workspace():
    """Saves workspace file to load on next session."""
    acknowledge = raw_input('Do you want to save your work? y/n ')
    if acknowledge == 'y':
        save_workspace()
        print 'Workspace saved. Goodbye!'
    elif acknowledge == 'n':
        print 'Goodbye...'
