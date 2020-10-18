# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
from contextlib import contextmanager

#custom context manager mimicing with statement for file handling
@contextmanager
def open_file(file, mode):
    try:
        f=open(file, mode)
        yield f
    finally:
        f.close()
    
with open_file('sample.txt', 'w') as f:
    f.write('Testing')
    
print(f.closed)

#contxt manager to change directory and print the files in there and change
#back to original directory
#can be modified to work with db, locks, etc
@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)
    
with change_dir('dir1'):
    print(os.listdir())