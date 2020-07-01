# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 11:38:37 2020

@author: bobeep
"""


def maxProfit(prices):
    n = len(prices)
    profit = [0]
    for i in range(1, n):
        profit.append(max(profit[-1]+prices[i]-prices[i-1], 0))
    return max(profit)

prices =  [7,6,4,3,1]
profit = maxProfit(prices)





class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        profit = [0]
        for i in range(1, n):
            profit.append(max(profit[-1]+prices[i]-prices[i-1], 0))
        return max(profit)
    
#%% 别人的答案
def maxProfit(prices):
    max_profit, min_price = 0, float('inf')
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit