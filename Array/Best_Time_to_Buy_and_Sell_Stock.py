# Two Sum
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far = float('inf')
        profit = 0
        for price in prices:
            profit = max(profit,price-min_so_far)
            min_so_far = min(min_so_far,price)
        return profit