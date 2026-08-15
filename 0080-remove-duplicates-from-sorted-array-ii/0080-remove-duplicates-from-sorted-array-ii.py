class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        k=0
        for j in d:
            c=min(d[j],2)
            for x in range(c):
                nums[k]=j
                k+=1
        return k
