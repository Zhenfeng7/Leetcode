class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        if len(prices) < 2: return max
        
        low = prices[0]
        for i in prices[1:]:
            if i < low:
                low = i
            else:
                if i - low > max:
                    max = i - low
        return max
        