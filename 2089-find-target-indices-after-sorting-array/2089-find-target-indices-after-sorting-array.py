class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
      s=[]
      i=0
      while i<(len(nums)-1):
            if nums[i]>nums[i+1]:
                nums[i],nums[i+1]=nums[i+1],nums[i]
                i=0

            else: 
                i+=1
      result=[]
      for i in range(len(nums)):
        if target==nums[i]:
            result.append(i)
      return result


        