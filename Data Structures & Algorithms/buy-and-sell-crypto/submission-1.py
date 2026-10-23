class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        max_profit = 0
        while i < len(prices):
            j = len(prices) - 1
            while j > i:
                currecnt_profit = prices[j] - prices[i]
                if currecnt_profit > max_profit:
                    max_profit = currecnt_profit
                j -= 1
            i += 1
        return max_profit
