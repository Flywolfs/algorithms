# -*- encoding: utf-8 -*-
'''
@File    :   mini_coins.py
@Author :   Chi Zhang
'''
class Solution:
    def coinChange(self, coins, amount: int):
        records = dict()
        return self.counts(records,coins,amount)

    def counts(self,records,coins,amount):
        amounts = list()
        if len(coins) == 0:
            return -1
        if amount == 0:
            return 0
        if min(coins) > amount:
            return -1
        for coin in coins:
            if amount - coin >= 0:
                if amount - coin in records:
                    temp = records[amount - coin]
                else:
                    temp = self.counts(records,coins, amount - coin)
                    records[amount - coin] = temp
                result = temp + 1
                if result != 0:
                    amounts.append(result)
        if amounts != []:
            return min(amounts)
        else:
            return -1

if __name__=="__main__":
    coins = [1,2,5]
    amount = 100
    records = dict()
    sol = Solution()
    print(sol.coinChange(coins,amount))