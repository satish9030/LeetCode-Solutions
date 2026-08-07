class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s={}
        for i in range(len(nums)):
            t=target-nums[i]
            if t in s:
                return [s[t],i]
            s[nums[i]]=i
        