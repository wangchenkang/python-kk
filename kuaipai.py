#! /usr/bin/env python
# -*- coding: utf-8 -*-

def main(n):
    length = len(n)
    if length <= 1:
        return n
    else:
        middle = n[0]
        left = [i for i in n[1:] if i < middle]
        right = [i for i in n[1:] if i >= middle]
        return main(left) + [middle] + main(right) 

    
if __name__ == '__main__':
    print main([1,2,3,4,6,3,2,5,6])
