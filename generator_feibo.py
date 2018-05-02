#! /usr/bin/env python
# -*- coding: utf-8 -*-

import xlrd
import pymysql

def main(n):
    i,j = 0, 1
    while i < n:
        yield i
        i,j = j, i+j

    
if __name__ == '__main__':
    for i in main(5):
        print i
