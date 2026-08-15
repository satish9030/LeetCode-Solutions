class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        k=0
        s=0
        for i in range(1,len(prices)):
            c=prices[i]-prices[k]
            if c>0:
                s+=c
            k+=1
        return s