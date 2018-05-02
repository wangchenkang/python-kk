#! /usr/bin/env python
# -*- coding: utf-8 -*-

class Node(object):
    '''单链表逆置'''
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
list_node = Node(8, Node(7, Node(6, Node(5))))

def main(n):
    pre = n
    cur = n.next
    pre.next = None
    while cur:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
    return pre

if __name__ == '__main__':
    a = main(list_node)
    while a:
        print a.data
        a = a.next
