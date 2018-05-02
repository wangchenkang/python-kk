#! /usr/bin/env python
# -*- coding: utf-8 -*-

def main(n, a):
    length = len(n)
    if length < 1:
        return -1
    elif length ==1:
        if n[0] == a:
            return 0
        else:
            return -1
    else:
        low = 0
        high = length -1
        while low < high:
            middle = (low+high) // 2
            guess = n[middle]
            if guess < a:
                low += 1
            elif guess > a:
                high -= 1
            else:
                return middle

if __name__ == '__main__':
    print main([1,2,3,4,3,2,4,57,6], 4)
