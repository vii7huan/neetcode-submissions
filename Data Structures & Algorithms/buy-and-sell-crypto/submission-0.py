class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Input: prices = [10,1,5,6,7,1] Output: 6
        maxp= 0
        minbuy = prices[0]

        for sell in prices:
            maxp = max(maxp, sell - minbuy)
            minbuy = min(minbuy, sell)
        return maxp