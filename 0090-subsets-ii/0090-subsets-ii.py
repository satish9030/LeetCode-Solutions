class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        a=[[]]
       
        for i in nums:
            r=[]
            for j in a:
                r.append(j+[i])
            a+=r
        a=[list(x) for x in set(tuple(x) for x in a)]
        return a