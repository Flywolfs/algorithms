# -*- encoding: utf-8 -*-
'''
@File    :   lian_biao_fan_zhuan.py    
@Author :   Chi Zhang
'''
class Node(object):
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_

def reverse(cur):

    pre = None
    while cur != None:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
    return pre


if __name__ == '__main__':
    l1 = Node(3)
    l1.next = Node(2)
    l1.next.next = Node(1)
    l1.next.next.next = Node(9)
    print(l1.elem,l1.next.elem,l1.next.next.elem,l1.next.next.next.elem)
    l = reverse(l1)
    print(l.elem, l.next.elem, l.next.next.elem, l.next.next.next.elem)