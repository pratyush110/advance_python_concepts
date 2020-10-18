# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from contextlib import contextmanager

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