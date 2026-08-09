class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        maxprofit = 0
        for i in range(1,len(prices)):
            sell = prices[i]
            profit = sell - prices[buy]
            maxprofit = max(profit, maxprofit)
            if prices[i] < prices[buy]:
                buy = i
        return maxprofit
             
        


        