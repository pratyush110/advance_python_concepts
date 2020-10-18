#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 17:26:09 2020

@author: pratyush
"""

class Open_File():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type,exc_val, tracbeack):
        self.file.close()
        
with Open_File('sample.txt', 'w') as f:
    f.write('Testing')
    
#checking if file closed properly, should return True if closed
print(f.closed)