#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 11:18:53 2020

@author: pratyush
"""
#import threading
import time
import concurrent.futures

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

with concurrent.futures.ThreadPoolExecutor() as executor:
    #f1 = executor.submit(do_something, 1)
    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_something, secs)

#threads=[]
#
#for _ in range(10):
#    t=threading.Thread(target=do_something, args=[1.5])
#    t.start()
#    threads.append(t)
#
#for thread in threads:
#    thread.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')