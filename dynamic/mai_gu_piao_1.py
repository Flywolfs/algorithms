# -*- encoding: utf-8 -*-
'''
@File    :   mai_gu_piao_1.py    
@Author :   Chi Zhang
'''

class Solution:
    def maxProfit(self, prices):
        lowest_i = 0
        highest_i = 0
        if len(prices) == 1:
            return 0
        elif len(prices) == 0:
            return 0
        else:
            min_price =
            max_profig = 0
            for i in range(1,len(prices)):
                if i == 0 and prices[i] > prices[i+1]