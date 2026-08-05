class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # two pointer approach
        min_price = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            curr = prices[i]
            profit = max(profit, curr-min_price)
            min_price = min(curr, min_price)
        return profit


        