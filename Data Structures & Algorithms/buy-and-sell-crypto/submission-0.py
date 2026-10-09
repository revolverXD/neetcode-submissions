class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_p = 0
        sell_p = 1
        while buy_p < len(prices)-1:
            if (prices[sell_p] - prices[buy_p]) > max_profit:
                max_profit = (prices[sell_p] - prices[buy_p])
            sell_p +=1
            if sell_p == len(prices):
                buy_p += 1
                sell_p = buy_p + 1
        return max_profit