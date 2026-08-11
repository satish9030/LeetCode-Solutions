class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        s=nums[0]
        for i in range(1,len(nums)):
            
            if nums[i]==nums[i-1]+1:
                s+=nums[i]
            else:
                break
        r=set(nums)
        while s in r:
            s+=1
        return s
        