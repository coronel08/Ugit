import os
from . import data

def write_tree(directory='.'):
    with os.scandir(directory) as it:
        for entry in it:
            full = f'{directory}/{entry.name}'
            if entry.is_file (follow_symlinks=False):
                #TODO write the file object store here
                print(full)
            elif entry.is_dir(follow_symlinks=False):
                write_tree(full)

    #TODO actually create the tree object
