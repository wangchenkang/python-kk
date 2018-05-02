#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
from multiprocessing import Value, Process, Queue, Array, RLock

def main(n, a):
    n.value = 3.14
    a[0] = 5

num = Value('d', 0.0)
arr = Array('i', range(10))
for i in range(4):
    p = Process(target=main, args=(num, arr))
    p.start()
    p.join()
print num.value
print arr[:]
