'''Namespace functionality'''

import pickle

name_space = {}

def save_workspace(filename='filename.mat'):
    """Save current workspace"""
    pickle.dump(name_space, open(filename, 'wb'))

def load_workspace(filename='filename.mat'):
    """Loads saved workspace"""
    try:
        name_space = pickle.load(open(filename, 'rb'))
        return name_space
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
