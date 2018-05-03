#! /usr/bin/env python
# -*- coding: utf-8 -*-

def main(stra, strb):
    f = 0
    list_ = list()
    lengtha = len(stra)
    lengthb = len(strb)
    length = max(lengtha, lengthb)
    if lengtha < length:
        stra = '0'*(length-lengtha) + stra
    if lengthb < length:
        strb = '0'*(length-lengthb) + strb
    
    for i in range(1, length+1):
        c = int(stra[-i]) + int(strb[-i]) + f 
        d = c / 3
        e = c % 3
        if i == 1:
            if c < 3:
                list_.append(c)
                f = 0
            else:
                list_.append(e)
                f = d
        else:
            if c < 3:
                list_.insert(0,c)
                f = 0
            else:
                list_.insert(0,e)
                f = d
    
    return ''.join([str(i) for i in list_])

    
if __name__ == '__main__':
    print main('0101', '12102')
