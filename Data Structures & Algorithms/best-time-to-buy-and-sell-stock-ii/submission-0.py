class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1
        profit = 0

        while i < j and j < len(prices):
            if prices[i] < prices[j]:
                while j < len(prices) - 1 and prices[j] < prices[j + 1]:
                    j += 1

                profit += prices[j] - prices[i]
                i = j + 1
                j += 1
            else:
                i += 1
            
            j += 1

        return profit