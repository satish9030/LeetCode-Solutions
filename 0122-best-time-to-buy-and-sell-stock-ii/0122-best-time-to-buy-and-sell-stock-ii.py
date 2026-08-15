class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        s=0
        for i in range(1,len(prices)):
            c=prices[i]-prices[i-1]
            if c>0:
                s+=c
        return s