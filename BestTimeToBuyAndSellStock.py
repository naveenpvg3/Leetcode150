class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                curr_profit = prices[r] - prices[l]
                maxP = max(curr_profit, maxP)
            else:
                left = right
            right += 1
        return maxP
    
    # T- O(n) S - O(1)