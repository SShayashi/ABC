from typing import List


class Solution:
    # def maxProfit(self, prices: List[int]) -> int:
    #     length = len(prices)
    #     ans = 0
    #     for x in range(length):
    #         for y in range(x+1, length):
    #             if prices[x] < prices[y]:
    #                 ans = max(prices[y]-prices[x], ans)
    #     return ans
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        if length <= 1:
            return 0
        mini = prices[0]
        maxiprofit = 0
        for x in range(1, length):
            if prices[x] < mini:
                mini = prices[x]
            maxiprofit = max(maxiprofit, prices[x] - mini)
        return maxiprofit

print(Solution().maxProfit([2,1,2,0,1]))