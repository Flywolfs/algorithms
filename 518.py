# -*- encoding: utf-8 -*-
'''
@File    :   coins_comb.py    
@Author :   Chi Zhang
'''

class Solution:
    def change(self, amount, coins):
        records = dict()
        if len(coins) == 0:
            return 0
        if amount == 0:
            return 0
        if min(coins) > amount:
            return 0
        result = self.search(records, coins, amount)
        if result == []:
            return 0
        else:
            return len(result)

    def search(self,records,coins,amount):
        #去重的list
        comb = list()
        print(records)
        for coin in coins:
            temp = list()
            if amount - coin > 0:
                if amount - coin in records:
                    temp = records[amount - coin]
                else:
                    temp = self.search(records,coins,amount - coin)
                    records[amount - coin] = temp
                for i in temp:
                    i.append(coin)
                    if i not in comb:
                        comb.append(i)
            elif amount -coin == 0:
                if 0 in records:
                    records[0].append(coin)
                else:
                    records[0] = [coin]

        return comb

if __name__=="__main__":
    coins = [1,2,5]
    amount = 5
    sol = Solution()
    print(sol.change(amount,coins))