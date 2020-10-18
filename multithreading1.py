#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 11:18:53 2020

@author: pratyush
"""
import time

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

do_something(1)
do_something(1)

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')