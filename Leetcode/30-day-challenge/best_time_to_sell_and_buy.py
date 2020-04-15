# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3287/

"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        buy_index = sell_index = 0
        max_profit = 0

        while buy_index < len(prices) and sell_index < len(prices):
            while sell_index < len(prices) - 1 and prices[sell_index + 1] > prices[sell_index]:
                sell_index += 1

            current_profit = prices[sell_index] - prices[buy_index]
            max_profit += max(0, current_profit)

            buy_index = sell_index + 1
            sell_index = buy_index
        
        return max_profit


s = Solution()

example1 = [7,1,5,3,6,4]
print(s.maxProfit(example1), " Expected: 7")

example2 = [1,2,3,4,5]
print(s.maxProfit(example2), "Expected: 4")

example3 = [7,6,4,3,1]
print(s.maxProfit(example3), "Expected: 0")