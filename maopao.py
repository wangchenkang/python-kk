#! /usr/bin/env python
# -*- coding: utf-8 -*-

def main(n):
    length = len(n)
    if length <= 1:
        return n
    else:
        for i in range(length-1):
            for j in range(length-i-1):
                if n[j] > n[j+1]:
                    n[j], n[j+1] = n[j+1], n[j]
        return n

    
if __name__ == '__main__':
    print main([1,2,3,4,6,3,2,5,6])
