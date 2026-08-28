class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d = {}
        r = []
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1
        for i in d:
            if d[i] == 2:
                r.append(i)
        return r