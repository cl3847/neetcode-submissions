class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = prices[0]
        best_sell = 0

        for n in prices:
            lowest_price = min(lowest_price, n)
            best_sell = max(best_sell, n - lowest_price)
        
        return best_sell