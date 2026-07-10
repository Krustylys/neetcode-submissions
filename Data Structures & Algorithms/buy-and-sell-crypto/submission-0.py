class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        #brute-force

        profit = 0

        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if profit < prices[j] - prices[i]:
                    profit = prices[j] - prices[i]
        
        if profit > 0:
            return profit
        else:
            return 0

        