#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import xlrd
import pymysql
from multiprocessing import Process, Queue, Array, RLock

FILE_SIZE= 0
WORKERS = 4
BLOCK_SIZE = 0
file = '/root/course.xlsx'

def get_file_size(file):
    global FILE_SIZE
    fs = open(file, 'rb')
    fs.seek(0, os.SEEK_END)
    FILE_SIZE = fs.tell()
    fs.close()


def main():
    global BLOCK_SIZE
    get_file_size(file)
    BLOCK_SIZE = FILE_SIZE/WORKERS
    rlock = RLock()
    array = Array('1', WORKERS)
    print array
if __name__ == '__main__':
    main()
