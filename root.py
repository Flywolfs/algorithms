# -*- encoding: utf-8 -*-
'''
@File    :   root.py    
@Author :   Chi Zhang
'''

def root2(n):
    x = n
    k = 2
    prev = 0.0
    while abs(prev-x) > 0.000000000001:
        prev = x
        x = (x*x+k)/(2*x)
    print(x)

root2(2)